def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_digits(n):
        return int(str(n)[1:-1])
    x = numbers[803]
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            if set(str(i)) == {'2', '3', '5', '7'} and set(str(remove_digits(i))) < {'2', '3', '5', '7'}:
                primes.append(i)
    return sorted(primes)