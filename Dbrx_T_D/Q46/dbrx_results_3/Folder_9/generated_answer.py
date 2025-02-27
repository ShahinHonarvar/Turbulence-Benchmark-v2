import math

def gcf_three_nums(nums):
    a = nums[66]
    b = nums[90]
    c = nums[27]
    gcd_ab = math.gcd(a, b)
    return math.gcd(gcd_ab, c)