def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[29]
    res = []
    for i in range(2, x):
        j = i
        while j != 0:
            if is_prime(j):
                j //= 10
            else:
                break
        if j == 0:
            res.append(i)
    return sorted(res, reverse=True)