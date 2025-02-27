from math import sqrt

def all_right_truncatable_prime(nums):
    result = []
    x = nums[78]
    for i in range(2, x):
        if is_prime(i) and is_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[:i])):
            return False
    return True