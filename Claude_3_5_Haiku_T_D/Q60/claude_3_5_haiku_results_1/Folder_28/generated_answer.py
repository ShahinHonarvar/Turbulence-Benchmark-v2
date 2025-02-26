def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[19]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    if not is_prime(num):
        return False
    left_truncatable = True
    right_truncatable = True
    num_str = str(num)
    while len(num_str) > 1:
        num_str = num_str[1:]
        if not is_prime(int(num_str)):
            left_truncatable = False
            break
    num_str = str(num)
    while len(num_str) > 1:
        num_str = num_str[:-1]
        if not is_prime(int(num_str)):
            right_truncatable = False
            break
    return left_truncatable and right_truncatable