def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 9:
        n_str = str(n)
        n_str_left = n_str[1:]
        n_str_right = n_str[:-1]
        left_num = int(n_str_left)
        right_num = int(n_str_right)
        if not (is_prime(left_num) and is_prime(right_num)):
            return False
        n = left_num if len(n_str_left) > 1 else left_num
    return is_prime(n)

def all_left_right_truncatable_prime(nums):
    x = nums[74]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)