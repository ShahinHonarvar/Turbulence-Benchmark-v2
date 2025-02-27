import math

def gcf_three_nums(nums):
    a = nums[742]
    b = nums[888]
    c = nums[629]
    return math.gcd(math.gcd(a, b), c)