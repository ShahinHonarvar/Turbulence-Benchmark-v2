def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[466]
    res = []
    for i in range(x, 1, -1):
        if '0' in str(i):
            continue
        while i >= 10 and is_prime(i):
            i = int(str(i)[1:-1])
            if i and i not in res:
                res.append(int(str(i)) * 10 + i)
        if i < 10 and is_prime(i):
            res.append(i)
    return sorted(res, reverse=True)