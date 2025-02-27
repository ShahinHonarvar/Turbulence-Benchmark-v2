def all_left_truncatable_prime(t):
    x = t[24]
    res = []
    for i in range(2, x):
        if is_prime(i) and (not has_zero(i)):
            if is_left_truncatable(i):
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

def has_zero(i):
    return '0' in str(i)

def is_left_truncatable(i):
    str_i = str(i)
    for j in range(1, len(str_i)):
        if not is_prime(int(str_i[j:])):
            return False
    return True