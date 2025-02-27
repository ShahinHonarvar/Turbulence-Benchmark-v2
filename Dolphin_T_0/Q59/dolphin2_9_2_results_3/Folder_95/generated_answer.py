def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_t(n):
        if n == 0:
            return False
        else:
            while n > 0:
                if n % 10 == 0:
                    return False
                n //= 10
            return True
    x = t[77]
    res = []
    for n in range(2, x):
        if is_prime(n) and is_t(n):
            res.append(n)
    return sorted(res)