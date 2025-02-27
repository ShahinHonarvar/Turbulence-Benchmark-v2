import math

def gcf_three_nums(nums):
    a = nums[46]
    b = nums[84]
    c = nums[23]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)