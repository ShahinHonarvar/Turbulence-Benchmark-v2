from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    return gcd(gcd(nums[85], nums[36]), nums[54])