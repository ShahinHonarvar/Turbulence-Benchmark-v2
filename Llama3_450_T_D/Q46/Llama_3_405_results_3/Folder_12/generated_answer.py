import math

def gcf_three_nums(nums):
    num1 = nums[91]
    num2 = nums[45]
    num3 = nums[48]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf