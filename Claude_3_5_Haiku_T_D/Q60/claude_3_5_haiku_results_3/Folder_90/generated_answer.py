def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(len(str_num)):
        left_truncated = int(str_num[i:])
        right_truncated = int(str_num[:len(str_num) - i])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
    return is_prime(num)

def all_left_right_truncatable_prime(nums):
    x = nums[466]
    result = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result