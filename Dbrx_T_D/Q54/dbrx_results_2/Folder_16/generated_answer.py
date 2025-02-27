import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    while n > 1:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_right_truncatable_prime(t):
    x = t[792]
    result = []
    for num in range(1, x):
        if right_truncatable_prime(num):
            result.append(num)
    return sorted(result)