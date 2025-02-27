import math

def gcf_three_nums(nums):
    a, b, c = (nums[32], nums[54], nums[13])
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)