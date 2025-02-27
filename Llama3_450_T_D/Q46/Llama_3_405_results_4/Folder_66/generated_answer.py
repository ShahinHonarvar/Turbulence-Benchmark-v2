import math

def gcf_three_nums(nums):
    num1 = nums[92]
    num2 = nums[69]
    num3 = nums[95]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf