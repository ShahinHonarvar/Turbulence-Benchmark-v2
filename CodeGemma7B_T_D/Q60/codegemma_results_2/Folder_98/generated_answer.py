from math import sqrt

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def left_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        num = int(str_num[i:])
        if not is_prime(num):
            return False
    return True

def right_truncatable(num):
    str_num = str(num)
    for i in range(len(str_num) - 2):
        num = int(str_num[:-i - 2])
        if not is_prime(num):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[8]
    result = []
    for num in range(2, x + 1):
        num_str = str(num)
        if all((digit != '0' for digit in num_str)) and left_truncatable(num) and right_truncatable(num):
            result.append(num)
    result.sort(reverse=True)
    return result if result else []