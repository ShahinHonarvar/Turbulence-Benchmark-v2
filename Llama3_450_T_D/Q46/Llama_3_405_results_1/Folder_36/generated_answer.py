import math

def gcf_three_nums(nums):
    index1 = 427
    index2 = 761
    index3 = 148
    num1 = nums[index1]
    num2 = nums[index2]
    num3 = nums[index3]
    gcf = math.gcd(math.gcd(num1, num2), num3)
    return gcf