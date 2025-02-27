from math import sqrt

def prime_factors(nums):
    result = set()
    x = nums[33]
    while x != 1:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                x //= i
                result.add(i)
                break
    return result