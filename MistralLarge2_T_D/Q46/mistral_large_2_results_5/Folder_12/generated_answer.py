import math

def gcf_three_nums(nums):
    a = nums[91]
    b = nums[45]
    c = nums[48]
    return math.gcd(math.gcd(a, b), c)