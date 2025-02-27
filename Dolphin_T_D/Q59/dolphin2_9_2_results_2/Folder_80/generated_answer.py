def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        ori = n
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return is_prime(ori)
    res = []
    x = t[14]
    for i in range(x):
        if is_left_truncatable(i):
            res.append(i)
    return sorted(res, reverse=True)