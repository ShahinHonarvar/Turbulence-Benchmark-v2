import math

def gcf_three_nums(nums):
    a = nums[990]
    b = nums[671]
    c = nums[711]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)