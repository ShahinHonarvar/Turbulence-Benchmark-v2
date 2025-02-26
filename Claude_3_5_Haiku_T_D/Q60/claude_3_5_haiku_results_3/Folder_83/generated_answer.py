def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    str_orig = str(num)
    while len(str_orig) > 0:
        if not is_prime(int(str_orig)):
            return False
        str_orig = str_orig[1:]
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[24]
    result = []
    for num in range(11, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result