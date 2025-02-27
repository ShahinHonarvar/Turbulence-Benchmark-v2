def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    if not is_prime(n):
        return False
    while len(str_n) > 1:
        str_n = str_n[1:-1]
        if not is_prime(int(str_n)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[91]
    return sorted([i for i in range(2, x + 1) if left_right_truncatable_prime(i)])