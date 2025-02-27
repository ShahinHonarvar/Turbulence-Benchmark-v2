def all_left_right_truncatable_prime(t):
    x = t[52]

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(p):
        p = str(p)
        while len(p) > 1:
            if p[0] == '0' or not is_prime(int(p[1:] + p[:-1])):
                return False
            p = p[1:] + p[:-1]
        return True
    res = [p for p in range(x, 0, -1) if is_prime(p) and is_left_right_truncatable_prime(p)]
    return res