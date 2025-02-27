from functools import reduce

def gcd_two_nums(pair):
    return reduce(lambda x, y: math.gcd(x, y), pair)

def gcf_two_nums(nums):
    return gcd_two_nums([nums[29], nums[74]])