def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        left_truncated = int(num_str[1:])
        right_truncated = int(num_str[:-1])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
        num_str = str(left_truncated)
    return is_prime(int(num_str))

def all_left_right_truncatable_prime(nums):
    x = nums[57]
    result = []
    for num in range(x, 11, -1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return result