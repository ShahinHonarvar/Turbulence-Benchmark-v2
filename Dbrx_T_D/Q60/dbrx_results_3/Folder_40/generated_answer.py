import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(t):
    x = t[10]
    result = []
    for i in range(10, x + 1):
        if is_prime(i) and is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)