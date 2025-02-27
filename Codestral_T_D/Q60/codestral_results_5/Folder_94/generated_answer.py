def all_left_right_truncatable_prime(t):
    x = t[43]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncable(n):
        while n >= 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncable(n):
        while n >= 10:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True

    def is_left_right_truncable_prime(n):
        if is_prime(n) and is_left_truncable(n) and is_right_truncable(n):
            return True
        return False
    return sorted([n for n in range(2, x + 1) if is_left_right_truncable_prime(n)])