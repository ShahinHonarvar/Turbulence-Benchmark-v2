def is_prime(num):
    if num in {0, 1}:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable(num):
    if not is_prime(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_right_truncatable_prime(val):
    x = val[26]
    res = []
    for num in range(2, x):
        if is_right_truncatable(num):
            res.append(num)
    return sorted(res)