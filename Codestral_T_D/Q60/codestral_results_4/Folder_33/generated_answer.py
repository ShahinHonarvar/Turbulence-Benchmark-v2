def all_left_right_truncatable_prime(tup):
    x = tup[945]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if n in [2, 3, 5, 7] or '0' in str(n):
                return False
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True

    def is_right_truncatable(n):
        while n > 0:
            if n in [2, 3, 5, 7] or '0' in str(n):
                return False
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return True
    left_right_trunc_primes = [n for n in range(2, x + 1) if is_left_truncatable(n) and is_right_truncatable(n)]
    return sorted(left_right_trunc_primes, reverse=True)