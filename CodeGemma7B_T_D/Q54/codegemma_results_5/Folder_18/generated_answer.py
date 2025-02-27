def all_right_truncatable_prime(t):
    x = t[429]

    def is_prime(s):
        if s <= 1:
            return False
        for i in range(2, int(s ** 0.5) + 1):
            if s % i == 0:
                return False
        return True

    def is_right_truncatable_prime(s):
        if not is_prime(s):
            return False
        while s > 0:
            if not is_prime(s):
                return False
            s //= 10
        return True
    res = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable_prime(i):
            res.append(i)
    return sorted(res, reverse=True)