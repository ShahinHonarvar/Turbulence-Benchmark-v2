from math import sqrt

def left_truncatable_prime(num):
    digits = str(num)
    for i in range(1, len(digits)):
        test_num = int(digits[i:])
        if not is_prime(test_num) or '0' in str(test_num):
            return False
    return True

def right_truncatable_prime(num):
    digits = str(num)
    for i in range(len(digits) - 1):
        test_num = int(digits[:len(digits) - i - 1])
        if not is_prime(test_num) or '0' in str(test_num):
            return False
    return True

def is_prime(test_num):
    if test_num < 2:
        return False
    if test_num <= 3:
        return True
    if test_num % 2 == 0 or test_num % 3 == 0:
        return False
    i = 5
    while i * i <= test_num:
        if test_num % i == 0 or test_num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and left_truncatable_prime(num) and right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)