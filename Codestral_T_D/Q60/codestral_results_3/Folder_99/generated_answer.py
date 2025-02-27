def all_left_right_truncatable_prime(t):
    x = t[758]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def trunc_left(n):
        return int(str(n)[1:])

    def trunc_right(n):
        return int(str(n)[:-1])

    def lr_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = trunc_left(n)
            if not is_prime(n):
                return False
            n = trunc_right(n)
            if not is_prime(n):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if lr_truncatable_prime(i)])