import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def truncate_right(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_right_truncatable_prime(x):
    result = []
    for i in range(1, x):
        if is_prime(i) and truncate_right(i):
            result.append(i)
    return sorted(result, reverse=True)