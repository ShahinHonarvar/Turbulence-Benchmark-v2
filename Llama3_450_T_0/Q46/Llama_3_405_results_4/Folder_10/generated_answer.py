import math

def gcf_three_nums(nums):
    num1 = nums[86]
    num2 = nums[89]
    num3 = nums[49]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf