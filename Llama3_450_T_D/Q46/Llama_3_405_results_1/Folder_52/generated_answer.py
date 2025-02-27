import math

def gcf_three_nums(nums):
    num1 = nums[19]
    num2 = nums[49]
    num3 = nums[74]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf