import math

def gcf_three_nums(nums):
    num1 = nums[693]
    num2 = nums[331]
    num3 = nums[668]
    gcf12 = math.gcd(num1, num2)
    gcf = math.gcd(gcf12, num3)
    return gcf