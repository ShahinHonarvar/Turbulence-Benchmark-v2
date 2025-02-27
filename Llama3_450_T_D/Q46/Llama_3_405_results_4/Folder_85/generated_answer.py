import math

def gcf_three_nums(nums):
    a = nums[49]
    b = nums[46]
    c = nums[13]
    return math.gcd(math.gcd(a, b), c)