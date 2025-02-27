from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    str_num = str(num)
    str_num_len = len(str_num)
    for left_len in range(1, str_num_len):
        int_left_trunc = int(str_num[left_len:])
        if not is_prime(int_left_trunc):
            return False
        int_right_trunc = int(str_num[:str_num_len - left_len])
        if not is_prime(int_right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_nums):
    x = tuple_of_nums[67]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True) if result else []