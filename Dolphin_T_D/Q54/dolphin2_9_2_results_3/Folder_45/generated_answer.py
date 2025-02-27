def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[61]
    res = []
    for i in range(1, x):
        if is_prime(i):
            t = i
            while t != 0:
                if not is_prime(t):
                    break
                t //= 10
                if t == 0:
                    res.append(i)
    return sorted(res)