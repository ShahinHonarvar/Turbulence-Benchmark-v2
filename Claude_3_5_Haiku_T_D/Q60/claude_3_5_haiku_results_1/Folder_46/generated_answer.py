def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[33]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_truncatable(num):
            result.append(num)
    return sorted(result)

def is_truncatable(num):
    str_num = str(num)
    while len(str_num) > 1:
        left = int(str_num[1:])
        right = int(str_num[:-1])
        if not is_prime(left) or not is_prime(right):
            return False
        str_num = str(left)
    return is_prime(int(str_num))