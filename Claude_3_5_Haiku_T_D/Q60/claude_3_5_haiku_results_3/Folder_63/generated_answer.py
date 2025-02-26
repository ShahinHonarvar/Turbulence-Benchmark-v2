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
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    original_num = str(n)
    for i in range(len(original_num)):
        truncated = int(original_num[i:])
        if not is_prime(truncated):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[88]
    result = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(result)