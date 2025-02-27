import math

def gcf_three_nums(nums):
    num1 = nums[17]
    num2 = nums[88]
    num3 = nums[35]
    gcf1 = math.gcd(num1, num2)
    return math.gcd(gcf1, num3)