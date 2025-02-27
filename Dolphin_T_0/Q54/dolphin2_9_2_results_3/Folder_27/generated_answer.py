def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[79]
    r = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            j = i
            while j != 0 and j != 1 and (j != 2) and is_prime(j):
                j = int(str(j)[-1] + str(j)[:-1])
            if j == 0 or j == 1:
                r.append(i)
    return sorted(r, reverse=True)