def all_right_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[8]
    primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(primes, reverse=True) if primes else []