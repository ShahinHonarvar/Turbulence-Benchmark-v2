def all_left_truncatable_prime(tup):
    x = tup[618]
    res = []
    for i in range(2, x):
        if is_prime(i) and (not has_zero(i)):
            if is_left_truncatable(i):
                res.append(i)
    return sorted(res)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_zero(n):
    return '0' in str(n)

def is_left_truncatable(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True