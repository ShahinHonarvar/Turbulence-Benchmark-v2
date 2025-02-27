from math import sqrt

def all_left_right_truncatable_prime(a):
    x = a[36]
    result = []
    for n in range(2, x + 1):
        if is_prime(n) and (not contains_zero(n)) and check_truncatable(n):
            result.append(n)
    return sorted(result, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(n):
    return '0' in str(n)

def check_truncatable(n):
    s = str(n)
    for i in range(1, len(s)):
        left = int(s[:i])
        right = int(s[i:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True