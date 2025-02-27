import math

def gcf_three_nums(nums):
    num1 = nums[90]
    num2 = nums[54]
    num3 = nums[96]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf