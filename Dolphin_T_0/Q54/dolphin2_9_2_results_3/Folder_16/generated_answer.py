def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[792]
    res = []
    for i in range(x, 0, -1):
        if is_prime(i):
            if all(is_prime((int(str(i)[:-j]) for j in range(1, len(str(i)))))) and i < x:
                res.append(i)
    return sorted(res)