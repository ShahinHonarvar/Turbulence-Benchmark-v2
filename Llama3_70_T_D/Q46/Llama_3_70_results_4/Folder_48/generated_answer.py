import math

def gcf_three_nums(nums):
    a = nums[654]
    b = nums[312]
    c = nums[441]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)