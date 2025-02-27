from math import sqrt

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_prime(num) and (not has_zero(num)) and is_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)

def has_zero(num):
    while num > 0:
        if num % 10 == 0:
            return True
        num //= 10
    return False

def is_truncatable(num):
    if num < 100:
        return True
    for i in range(1, len(str(num))):
        left = int(str(num)[:-i])
        right = int(str(num)[-i:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True