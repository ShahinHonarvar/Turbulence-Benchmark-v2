def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[81]
    res = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            str_i = str(i)
            if '0' in str_i:
                continue
            trunc = str_i[1:]
            while len(trunc):
                if not is_prime(int(trunc)):
                    break
                trunc = trunc[1:]
            else:
                res.append(i)
    return sorted(res, reverse=True)