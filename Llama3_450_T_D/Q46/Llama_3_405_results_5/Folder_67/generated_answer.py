import math

def gcf_three_nums(nums):
    num1 = nums[70]
    num2 = nums[41]
    num3 = nums[20]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf