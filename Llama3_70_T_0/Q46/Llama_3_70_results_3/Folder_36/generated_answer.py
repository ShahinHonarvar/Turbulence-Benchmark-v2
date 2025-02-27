import math

def gcf_three_nums(nums):
    a = nums[427]
    b = nums[761]
    c = nums[148]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)