def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return True
        if n % 10 in (0, 2, 4, 5, 6, 8):
            return False
        return n // 10 % 10 in (0, 2, 4, 5, 6, 8) and is_right_truncatable(n // 10)
    res = []
    for n in range(2, x):
        if is_prime(n) and is_right_truncatable(n):
            res.append(n)
    return sorted(res)