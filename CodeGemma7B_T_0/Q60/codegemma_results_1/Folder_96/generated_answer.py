def all_left_right_truncatable_prime(t):
    x = t[29]
    res = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i):
            res.append(i)
    res.sort()
    return res

def is_prime(i):
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def is_truncatable(i):
    if '0' in str(i):
        return False
    for j in range(1, len(str(i))):
        if not is_prime(int(str(i)[:j])):
            return False
        if not is_prime(int(str(i)[-j:])):
            return False
    return True