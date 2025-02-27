import math

def gcf_three_nums(lst):
    nums = [lst[19], lst[49], lst[74]]
    return math.gcd(math.gcd(nums[0], nums[1]), nums[2])