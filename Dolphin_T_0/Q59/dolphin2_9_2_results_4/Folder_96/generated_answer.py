def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[29]
    res = []
    for num in range(2, x):
        if is_prime(num):
            trunc = str(num)
            while len(trunc) > 1:
                if is_prime(int(trunc)):
                    trunc = trunc[1:]
                else:
                    break
            else:
                res.append(num)
    return sorted(res)