import math

def gcf_three_nums(nums):
    a = nums[0]
    b = nums[8]
    c = nums[3]
    return math.gcd(math.gcd(a, b), c)