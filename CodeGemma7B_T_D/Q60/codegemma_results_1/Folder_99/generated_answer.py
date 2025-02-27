from math import sqrt

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def is_truncatable_prime(x):
    str_x = str(x)
    if '0' in str_x:
        return False
    for i in range(1, len(str_x)):
        left = int(str_x[:i])
        right = int(str_x[i:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return sorted(result)