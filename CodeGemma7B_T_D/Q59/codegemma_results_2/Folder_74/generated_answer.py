from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if num <= 1 or '0' in str(num):
        return False
    for i in range(1, len(str(num))):
        if not is_prime(int(str(num)[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    result = []
    for num in nums:
        if left_truncatable_prime(num) and num <= nums[36]:
            result.append(num)
    result.sort()
    return result