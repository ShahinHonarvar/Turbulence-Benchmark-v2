def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_trunc(n):
        return int(str(n)[1:]) if n >= 10 else n

    def right_trunc(n):
        return int(str(n)[:-1])

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = left_trunc(n)
            if not is_prime(n):
                return False
        n = t[4]
        while n >= 10:
            n = right_trunc(n)
            if not is_prime(n):
                return False
        return True
    return sorted([n for n in range(2, t[4] + 1) if is_left_right_truncatable_prime(n)])