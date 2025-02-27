def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[3]
    res = []
    for i in range(2, x):
        if is_prime(i):
            r = i
            while r > 0:
                if not is_prime(r):
                    break
                r //= 10
            else:
                res.append(i)
    return sorted(res, reverse=True)