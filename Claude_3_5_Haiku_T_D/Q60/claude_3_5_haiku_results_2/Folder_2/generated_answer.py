def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    while len(str_n) > 1:
        left_truncated = int(str_n[1:])
        right_truncated = int(str_n[:-1])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
        str_n = str(left_truncated)
    return is_prime(int(str_n))

def all_left_right_truncatable_prime(nums):
    x = nums[618]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)