from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n_str = str(n)
    for i in range(1, len(n_str)):
        left = int(n_str[i:])
        right = int(n_str[:-i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True

def all_left_right_truncatable_prime(tup, x):
    x = tup[41]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)