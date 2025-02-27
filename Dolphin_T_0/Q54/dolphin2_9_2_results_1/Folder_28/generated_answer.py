def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[19]
    res = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 1 and is_prime(j):
                j //= 10
            if j == 1:
                res.append(i)
    return sorted(res)