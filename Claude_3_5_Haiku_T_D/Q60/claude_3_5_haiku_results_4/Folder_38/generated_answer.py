def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[28]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_truncatable_prime(num):
    if '0' in str(num):
        return False
    if not is_prime(num):
        return False
    left_trunc = str(num)
    right_trunc = str(num)
    while len(left_trunc) > 1:
        left_trunc = left_trunc[1:]
        if not is_prime(int(left_trunc)):
            return False
    while len(right_trunc) > 1:
        right_trunc = right_trunc[:-1]
        if not is_prime(int(right_trunc)):
            return False
    return True