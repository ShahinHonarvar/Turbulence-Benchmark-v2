def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[100]
    res = []
    for i in range(1, x):
        if '0' in str(i):
            continue
        f = is_prime(i)
        while f:
            if i < 10:
                res.append(i)
                break
            f = is_prime(int(str(i)[1:]))
            i = int(str(i)[1:])
        else:
            break
    res = sorted(res, reverse=True)
    return res