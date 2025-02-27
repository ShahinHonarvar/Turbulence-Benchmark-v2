import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 10:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return is_prime(n)

def all_left_right_truncatable_prime(t):
    x = t[630]
    result = []
    for i in range(1, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)