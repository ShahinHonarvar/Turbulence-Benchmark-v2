import math

def gcf_three_nums(nums):
    a = nums[62]
    b = nums[96]
    c = nums[26]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)