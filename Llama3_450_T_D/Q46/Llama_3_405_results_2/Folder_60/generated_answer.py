import math

def gcf_three_nums(nums):
    num1 = nums[96]
    num2 = nums[53]
    num3 = nums[35]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf