import math

def gcf_three_nums(nums):
    num1 = nums[59]
    num2 = nums[93]
    num3 = nums[84]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf