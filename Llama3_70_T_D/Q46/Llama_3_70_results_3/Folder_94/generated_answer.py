import math

def gcf_three_nums(nums):
    a = nums[56]
    b = nums[88]
    c = nums[51]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)