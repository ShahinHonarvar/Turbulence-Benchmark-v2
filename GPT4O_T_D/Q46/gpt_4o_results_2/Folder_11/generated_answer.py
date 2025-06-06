from math import gcd
from functools import reduce

def gcf_three_nums(nums):
    indices = [37, 30, 48]
    selected_numbers = [nums[i] for i in indices]
    return reduce(gcd, selected_numbers)