def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[71]
    res = []
    for i in range(x, 0, -1):
        if is_prime(i) and '0' not in str(i):
            j = i
            while j != 0:
                if not is_prime(int(str(j).replace(str(j)[-1], ''))):
                    break
                j = int(str(j).replace(str(j)[-1], ''))
            else:
                res.append(i)
    return sorted(res, reverse=True)