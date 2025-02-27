import math

def gcf_three_nums(nums):
    num1 = nums[27]
    num2 = nums[85]
    num3 = nums[51]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf