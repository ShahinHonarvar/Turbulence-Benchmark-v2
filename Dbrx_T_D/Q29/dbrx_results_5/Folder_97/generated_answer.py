import math

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return abs(a)

def gcf_two_nums(nums):
    if nums[180] == 0:
        return 0
    if nums[312] == 0:
        return 0
    return int(math.sqrt(nums[180] * nums[312]) * gcd(nums[180], nums[312]))