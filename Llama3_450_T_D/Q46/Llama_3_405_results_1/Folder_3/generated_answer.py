import math

def gcf_three_nums(nums):
    idx1 = 31
    idx2 = 69
    idx3 = 40
    num1 = nums[idx1]
    num2 = nums[idx2]
    num3 = nums[idx3]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf