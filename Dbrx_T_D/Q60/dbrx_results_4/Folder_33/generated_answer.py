import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_and_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 9:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    while n > 9:
        n = int(str(n)[:-1])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[945]
    result = []
    for i in range(10, x + 1):
        if is_left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)