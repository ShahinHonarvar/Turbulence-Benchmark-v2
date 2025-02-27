def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def drop_right_digit(n):
        return int(str(n)[:-1])
    x = numbers[86]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            n = i
            while n != 1 and is_prime(n):
                n = drop_right_digit(n)
            if n == 1:
                primes.append(i)
    return sorted(primes, reverse=True)