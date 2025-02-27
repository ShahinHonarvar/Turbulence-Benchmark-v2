import math

def gcf_three_nums(nums):
    a = nums[90]
    b = nums[41]
    c = nums[95]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)