import math

def gcf_three_nums(nums):
    a = nums[90]
    b = nums[54]
    c = nums[96]
    return math.gcd(a, math.gcd(b, c))