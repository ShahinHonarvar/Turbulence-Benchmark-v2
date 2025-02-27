from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left_and_right(k):
    if len(str(k)) < 2:
        return [k]
    result = []
    for i in range(1, len(str(k))):
        left = int(str(k)[i:])
        right = int(str(k)[:-i])
        if is_prime(left) and is_prime(right):
            result.append(k)
    return result

def all_left_right_truncatable_prime(t):
    x = t[11]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)

def is_left_and_right_truncatable_prime(k):
    if '0' in str(k):
        return False
    while k > 9:
        k = truncate_left_and_right(k)[0]
    return is_prime(k)