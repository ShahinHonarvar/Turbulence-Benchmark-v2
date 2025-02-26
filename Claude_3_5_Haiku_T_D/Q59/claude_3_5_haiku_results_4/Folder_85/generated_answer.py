def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_check(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(nums):
    x = nums[94]
    result = []
    for num in range(10, x):
        str_num = str(num)
        if '0' not in str_num and left_truncatable_check(num):
            result.append(num)
    return sorted(result)