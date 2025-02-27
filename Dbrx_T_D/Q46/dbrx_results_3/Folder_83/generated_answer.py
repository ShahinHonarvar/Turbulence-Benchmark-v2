import math

def gcf_three_nums(nums):

    def gcd(a, b):
        return math.gcd(a, b) if b else a
    num1 = nums[56]
    num2 = nums[54]
    num3 = nums[13]
    return gcd(num1, gcd(num2, num3))