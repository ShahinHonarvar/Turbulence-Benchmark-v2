import math

def gcf_two_nums(nums):

    def gcd(a, b):
        return gcd(b, a % b) if b else a
    return math.gcd(nums[166], nums[106])