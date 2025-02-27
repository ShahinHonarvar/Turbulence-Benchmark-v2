import math

def is_prime(num):
    if num != int(num):
        return False
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    num = int(num)
    while num > 0:
        num = int(num / 10)
        if not is_prime(num):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[767]
    result = ([],)
    for num in range(x - 1, 1, -1):
        if is_right_truncatable_prime(num):
            result = [num] + result
    return result