def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[758]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_truncatable_prime(num):
    num_str = str(num)
    while len(num_str) > 1:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:-1]
    return is_prime(int(num_str))