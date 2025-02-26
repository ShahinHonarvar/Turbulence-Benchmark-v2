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
        left = int(n_str[1:])
        right = int(n_str[:-1])
        if not (is_prime(left) and is_prime(right)):
            return False
        n = left
    return is_prime(n)

def all_left_right_truncatable_prime(nums):
    x = nums[8]
    result = []
    for num in range(x, 11, -1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return result