def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 1:
            if not is_prime(n // 10):
                return False
            n = n // 10
        return True
    x = t[94]
    res = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            res.append(i)
    return sorted(res)