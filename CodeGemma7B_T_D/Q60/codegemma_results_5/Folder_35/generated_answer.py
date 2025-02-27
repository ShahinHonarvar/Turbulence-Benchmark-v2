from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    while num > 1:
        if not is_prime(num):
            return False
        num = int(str(num)[1:])
    return True

def right_truncatable_prime(num):
    while num > 1:
        if not is_prime(num):
            return False
        num = int(str(num)[:-1])
    return True

def all_left_right_truncatable_prime(limit):
    result = []
    for num in range(2, limit):
        if num % 10 == 0:
            continue
        if left_truncatable_prime(num) and right_truncatable_prime(num):
            result.append(num)
    return sorted(result)