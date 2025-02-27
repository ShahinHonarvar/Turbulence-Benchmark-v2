import math
from functools import reduce

def gcf_three_nums(nums):
    return reduce(math.gcd, [nums[92], nums[69], nums[95]])