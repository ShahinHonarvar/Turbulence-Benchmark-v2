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
    for length in range(len(num_str), 0, -1):
        left = num_str[:length]
        right = num_str[-length:]
        while len(left) > 0 and len(right) > 0:
            if not (is_prime(int(left)) and is_prime(int(right))):
                return False
            left = left[1:]
            right = right[:-1]
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[38]
    result = [num for num in range(x, 1, -1) if is_prime(num) and is_left_right_truncatable_prime(num)]
    return result