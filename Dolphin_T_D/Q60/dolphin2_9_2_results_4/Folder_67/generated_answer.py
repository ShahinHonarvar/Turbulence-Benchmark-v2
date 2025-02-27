def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[71]
    res = []
    for i in range(2, x + 1):
        if is_prime(i) and i % 10 != 0 and (i % 100 != 0):
            j = i
            while len(str(j)) > 2 and is_prime(int(str(j).slice(1, -1))):
                j = int(str(j).slice(1, -1))
            if len(str(j)) == 1 or is_prime(j):
                res.append(i)
    return res[::-1] or []