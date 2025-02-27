from math import gcd
from functools import reduce

def gcf_three_nums(rotation_nums):
    ind47 = rotation_nums[47]
    ind10 = rotation_nums[10]
    ind28 = rotation_nums[28]
    return reduce(gcd, (ind47, ind10, ind28))