def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqr = int(n ** 0.5)
        for divisor in range(3, sqr + 1, 2):
            if n % divisor == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 9:
            if n % 10 == 0:
                return False
            n //= 10
        return True
    x = tup[975]
    primes = [num for num in range(x + 1) if is_prime(num)]
    primes = [num for num in primes if is_truncatable(num)]
    primes = sorted(primes, reverse=True)
    return primes