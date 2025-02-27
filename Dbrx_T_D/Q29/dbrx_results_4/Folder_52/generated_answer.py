import math

def gcf_two_nums(nums):

    def gcd(a, b):
        return math.gcd(a, b) if b != 0 else a
    num1 = nums[41]
    num2 = nums[90]
    return gcd(num1, num2)