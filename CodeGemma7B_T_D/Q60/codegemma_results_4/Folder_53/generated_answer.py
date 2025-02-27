def all_left_right_truncatable_prime(args):
    maximum = max(args)
    result = []
    for p in range(2, maximum + 1):
        if left_right_truncatable_prime(p):
            result.append(p)
    return sorted(result, reverse=True)

def left_right_truncatable_prime(x):
    if x <= 1 or not is_prime(x) or '0' in str(x):
        return False
    n = len(str(x))
    for i in range(1, n):
        left, right = (int(str(x)[:-i]), int(str(x)[i:]))
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True