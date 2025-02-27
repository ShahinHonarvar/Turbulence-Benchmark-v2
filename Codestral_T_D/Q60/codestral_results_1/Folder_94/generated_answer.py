def all_left_right_truncatable_prime(t):
    x = t[43]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if n not in primes:
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True

    def is_right_truncatable(n):
        while n > 0:
            if n not in primes:
                return False
            n = n // 10
        return True
    for i in range(2, x + 1):
        if is_prime(i) and '0' not in str(i):
            primes.append(i)
            if is_left_truncatable(i) and is_right_truncatable(i):
                primes.sort()
    return primes