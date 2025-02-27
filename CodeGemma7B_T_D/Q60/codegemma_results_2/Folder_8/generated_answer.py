def is_prime(n):
    if n <= 1 or (n > 2 and n % 2 == 0):
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def truncate_left(p):
    tmp = p
    val = 0
    while tmp:
        val = val * 10 + tmp % 10
        tmp //= 10
    return val

def truncate_right(p):
    tmp = p
    val = 0
    while tmp:
        val = val * 10 + tmp % 10
        tmp //= 10
    return val

def all_left_right_truncatable_prime(arg):
    res = []
    x = arg[41]
    for p in range(2, x + 1):
        if '0' in str(p):
            continue
        if not is_prime(p):
            continue
        if is_prime(truncate_left(p)) and is_prime(truncate_right(p)):
            res.append(p)
    return sorted(res, reverse=True) if res else []