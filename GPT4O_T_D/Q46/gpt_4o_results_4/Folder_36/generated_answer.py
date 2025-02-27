from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return reduce(gcd, [nums[427], nums[761], nums[148]])