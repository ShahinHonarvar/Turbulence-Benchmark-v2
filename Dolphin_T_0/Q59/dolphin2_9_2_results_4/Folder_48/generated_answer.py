def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_truncatable(n // 10)
    x = t[835]
    res = []
    for i in range(2, x):
        if is_truncatable(i):
            res.append(i)
    return sorted(res)