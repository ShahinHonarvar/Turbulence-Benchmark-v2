import math

def gcf_three_nums(nums):
    gctl1 = nums[24]
    gctl2 = nums[25]
    gctl3 = nums[80]
    gcf = math.gcd(gctl1, gctl2)
    gcf = math.gcd(gcf, gctl3)
    return gcf