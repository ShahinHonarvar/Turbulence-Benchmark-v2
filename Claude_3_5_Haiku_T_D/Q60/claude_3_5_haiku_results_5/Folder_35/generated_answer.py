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
    digits = len(str(n))
    num = n
    while num > 0:
        if num < 10:
            return is_prime(num)
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[177]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)