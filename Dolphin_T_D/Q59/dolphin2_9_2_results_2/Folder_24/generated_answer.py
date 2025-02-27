def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    res = []
    x = tup[65]
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i):
            j, k = (i, i)
            while k != 0:
                k = k // 10
                if not is_prime(j):
                    break
                j = k
            else:
                res.append(i)
    return sorted(res, reverse=True)