from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    indices = [10, 55, 36]
    selected_numbers = [nums[i] for i in indices if i < len(nums)]
    return reduce(gcd, selected_numbers)