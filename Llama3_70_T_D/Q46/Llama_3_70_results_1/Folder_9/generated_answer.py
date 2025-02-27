import math

def gcf_three_nums(nums):
    a = nums[66]
    b = nums[90]
    c = nums[27]
    ab_gcf = math.gcd(a, b)
    return math.gcd(ab_gcf, c)