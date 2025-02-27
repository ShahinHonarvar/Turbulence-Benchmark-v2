def all_left_truncatable_prime(tup):
    x = tup[41]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_trunc_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = n // 10
            if not is_prime(n):
                return False
        return True
    return sorted([n for n in range(2, x) if is_left_trunc_prime(n)])