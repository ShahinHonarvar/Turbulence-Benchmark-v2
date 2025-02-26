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
        left_truncated = int(n_str[1:])
        right_truncated = int(n_str[:-1])
        if not is_prime(left_truncated) or not is_prime(right_truncated):
            return False
        n = left_truncated
    return is_prime(n)

def all_left_right_truncatable_prime(nums):
    x = nums[835]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)