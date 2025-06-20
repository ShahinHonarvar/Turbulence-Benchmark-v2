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
    str_n = str(n)
    while len(str_n) > 1:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:-1]
    return is_prime(int(str_n))

def all_left_right_truncatable_prime(nums):
    x = nums[20]
    result = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result