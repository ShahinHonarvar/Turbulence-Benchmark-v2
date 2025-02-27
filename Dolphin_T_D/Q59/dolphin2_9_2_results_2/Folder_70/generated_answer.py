def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[433]
    res = []
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            sn = str(n)
            tag = True
            for i in range(len(sn)):
                if is_prime(int(sn[i:])):
                    if sn[i] == '0':
                        tag = False
                        break
            if tag:
                res.append(n)
    return sorted(res, reverse=True)