def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, d):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[945]
    primes = [n for n in range(2, x) if is_prime(n) and is_truncatable(n, 10)]
    return sorted(primes, reverse=True)