def all_left_right_truncatable_prime(nums):
    x = nums[758]
    res = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_truncatable_prime(num):
            res.append(num)
    return sorted(res)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        left = int(str_num[i:])
        right = int(str_num[:-i])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True