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
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def truncate_right(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(tup):
    x = tup[37]
    result = []
    for num in range(1, x):
        if is_prime(num) and truncate_right(num):
            result.append(num)
    return sorted(result, reverse=True)