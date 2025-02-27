def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        if '0' in str(i) or not is_prime(i):
            continue
        if is_prime(int(str(i)[1:-1])):
            primes.append(i)
    return sorted(primes)