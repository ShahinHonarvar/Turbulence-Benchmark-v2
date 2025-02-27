def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(len(str_num)):
        left_truncate = int(str_num[i:])
        right_truncate = int(str_num[:len(str_num) - i])
        if not (is_prime(left_truncate) and is_prime(right_truncate)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    if len(nums) < 101:
        return []
    x = nums[100]
    result = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(result, reverse=True)