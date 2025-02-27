import math

def gcf_three_nums(nums):

    def gcd(a, b):
        return math.gcd(a, b)
    num1 = nums[38]
    num2 = nums[52]
    num3 = nums[69]
    return math.gcd(gcd(num1, num2), num3)