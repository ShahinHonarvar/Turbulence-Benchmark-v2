import math

def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[69]
    num3 = nums[97]
    gcf12 = math.gcd(num1, num2)
    gcf = math.gcd(gcf12, num3)
    return gcf