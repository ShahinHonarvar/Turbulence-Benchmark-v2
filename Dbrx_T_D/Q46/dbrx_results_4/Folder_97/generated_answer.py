import math

def gcf_three_nums(nums):

    def gcd(a, b):
        return math.gcd(a, b)
    return gcd(gcd(nums[944], nums[814]), nums[865])