def all_left_truncatable_prime(t):

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n in prime_cache:
            return prime_cache[n]
        if n % 2 == 0 and n > 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        prime_cache[n] = True
        return True
    x = t[992]
    prime_cache = {2: True}
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])