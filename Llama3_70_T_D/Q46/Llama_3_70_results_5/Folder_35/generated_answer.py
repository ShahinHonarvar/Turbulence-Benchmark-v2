import math

def gcf_three_nums(nums):
    a = nums[742]
    b = nums[888]
    c = nums[629]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)