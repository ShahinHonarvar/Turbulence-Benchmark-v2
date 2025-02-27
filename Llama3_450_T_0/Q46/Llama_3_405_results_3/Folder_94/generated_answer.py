import math

def gcf_three_nums(nums):
    num1 = nums[56]
    num2 = nums[88]
    num3 = nums[51]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf