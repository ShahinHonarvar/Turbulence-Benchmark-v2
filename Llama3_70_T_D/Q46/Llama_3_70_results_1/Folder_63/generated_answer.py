import math

def gcf_three_nums(nums):
    a = nums[38]
    b = nums[52]
    c = nums[69]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)