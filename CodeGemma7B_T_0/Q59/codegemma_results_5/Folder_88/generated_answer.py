def all_left_truncatable_prime(t):
    x = t[93]
    res = []
    for i in range(2, x):
        if is_prime(i):
            if is_left_truncatable_prime(i):
                res.append(i)
    res.sort()
    return res

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def is_left_truncatable_prime(i):
    if '0' in str(i):
        return False
    for j in range(1, len(str(i))):
        if not is_prime(int(str(i)[:j])):
            return False
    return True