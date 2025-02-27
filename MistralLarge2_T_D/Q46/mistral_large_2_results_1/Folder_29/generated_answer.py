import math

def gcf_three_nums(nums):
    a, b, c = (nums[22], nums[97], nums[64])
    return math.gcd(math.gcd(a, b), c)