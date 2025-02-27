import math

def gcf_three_nums(nums):
    a = nums[477]
    b = nums[696]
    c = nums[663]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)