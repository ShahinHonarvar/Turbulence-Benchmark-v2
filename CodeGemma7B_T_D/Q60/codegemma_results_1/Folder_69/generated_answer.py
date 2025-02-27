from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    if not is_prime(int(str_num)):
        return False
    return True

def right_truncatable_prime(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[:-i])):
            return False
    if not is_prime(int(str_num)):
        return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[760]
    result = []
    for num in range(2, x + 1):
        if str(num).count('0') == 0 and left_truncatable_prime(num) and right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)