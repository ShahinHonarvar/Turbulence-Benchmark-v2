def all_left_truncatable_prime(t):
    x = t[39]
    res = []
    for i in range(2, x):
        if miller_rabin(i):
            for j in range(1, len(str(i))):
                if not miller_rabin(int(str(i)[j:])):
                    break
            else:
                res.append(i)
    return sorted(res, reverse=True)