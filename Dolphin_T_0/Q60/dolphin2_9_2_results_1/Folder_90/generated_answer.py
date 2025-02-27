def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[466]
    res = []
    if is_prime(x):
        res.append(x)
        temp = x
        while len(str(temp)) > 2:
            temp = int(str(temp)[1:-1])
            if is_prime(temp):
                res.append(temp)
            else:
                break
    return sorted(res, reverse=True)