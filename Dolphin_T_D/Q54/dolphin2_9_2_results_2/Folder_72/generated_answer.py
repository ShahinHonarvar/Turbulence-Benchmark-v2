def all_right_truncatable_prime(x):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        return is_truncatable(n // 10) and is_prime(n)
    res = []
    for i in range(x - 1, 0, -1):
        if is_truncatable(i):
            res.append(i)
    return res