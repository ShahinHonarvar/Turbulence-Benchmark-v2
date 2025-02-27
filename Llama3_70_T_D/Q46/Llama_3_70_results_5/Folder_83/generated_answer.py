import math

def gcf_three_nums(nums):
    a = nums[56]
    b = nums[54]
    c = nums[13]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)