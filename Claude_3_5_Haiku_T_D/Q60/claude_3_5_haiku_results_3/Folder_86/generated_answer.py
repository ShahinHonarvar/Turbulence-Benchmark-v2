def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[126]
    result = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_truncatable = True
        num_str = str(num)
        for i in range(len(num_str)):
            left_truncated = int(num_str[i:])
            right_truncated = int(num_str[:len(num_str) - i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            result.append(num)
    return result