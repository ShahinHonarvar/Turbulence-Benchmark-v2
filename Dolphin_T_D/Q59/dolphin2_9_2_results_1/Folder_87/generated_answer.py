def all_left_truncatable_prime(t):

    def is_prime(n):
        if n // 2 * 2 == n:
            return False
        i = 3
        sq = int(n ** 0.5)
        while i <= sq:
            if n % i == 0:
                return False
            i += 2
        return True
    x, res = (t[39], [])
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                res.append(i)
    return sorted(res, reverse=True)