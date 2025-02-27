import math

def gcf_three_nums(nums):
    num1 = nums[8]
    num2 = nums[2]
    num3 = nums[1]
    gcd_12 = math.gcd(num1, num2)
    return math.gcd(gcd_12, num3)