def all_right_truncatable_prime(t):
    x = t[36]
    res = []
    for i in range(2, x):
        if is_prime(i):
            if is_right_truncatable_prime(i):
                res.append(i)
    return sorted(res)

def is_prime(i):
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def is_right_truncatable_prime(i):
    if not is_prime(i):
        return False
    str_i = str(i)
    for j in range(1, len(str_i)):
        if not is_prime(int(str_i[:-j])):
            return False
    return True