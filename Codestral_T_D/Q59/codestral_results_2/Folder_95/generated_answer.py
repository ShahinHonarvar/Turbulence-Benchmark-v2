def all_left_truncatable_prime(t):
    x = t[77]
    primes = []

    def is_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if is_prime(n):
            while n > 0:
                n = n // 10
                if n > 0 and (not is_prime(n)):
                    return False
            return True
        return False
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)