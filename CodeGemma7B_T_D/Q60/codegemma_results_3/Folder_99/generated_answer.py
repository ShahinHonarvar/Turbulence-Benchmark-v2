from math import sqrt

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

def left_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def right_truncatable(num):
    str_num = str(num)
    for i in range(len(str_num) - 2, -1, -1):
        if not is_prime(int(str_num[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[758]
    result = []
    for num in range(2, x + 1):
        if left_truncatable(num) and right_truncatable(num) and (not str(num).startswith('0')):
            result.append(num)
    return sorted(result)