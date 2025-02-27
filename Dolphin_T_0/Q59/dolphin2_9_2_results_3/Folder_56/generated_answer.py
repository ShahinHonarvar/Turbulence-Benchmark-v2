def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[30]
    res = []
    for i in range(1, x):
        if '0' not in str(i):
            if is_prime(i):
                j = i
                while j != 0:
                    if not is_prime(j):
                        break
                    if j == 0:
                        res.append(i)
                        break
                    j //= 10
    res.sort()
    return res