def all_right_truncatable_prime(t):
    x = t[7]
    res = []
    for i in range(2, x):
        if is_prime(i):
            if is_right_truncatable(i):
                res.append(i)
    return sorted(res)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:-i])):
            return False
    return True