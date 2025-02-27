import math

def gcf_two_nums(nums):
    if len(nums) < 583:
        return None
    return math.gcd(nums[129], nums[582])