from math import sqrt

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def left_truncatable_prime(x):
    while x >= 10:
        x //= 10
        if not is_prime(x):
            return False
    return True

def right_truncatable_prime(x):
    digits = list(str(x))
    for i in range(1, len(digits)):
        digits.pop()
        num = int(''.join(digits))
        if not is_prime(num):
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and left_truncatable_prime(num) and right_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result