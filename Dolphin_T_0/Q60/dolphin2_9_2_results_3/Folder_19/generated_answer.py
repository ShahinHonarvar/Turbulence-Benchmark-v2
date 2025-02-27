def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_trunc(n):
        while n:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return True
    x = t[67]
    res = []
    for i in range(x, 0, -1):
        if is_trunc(i):
            res.append(i)
    return res