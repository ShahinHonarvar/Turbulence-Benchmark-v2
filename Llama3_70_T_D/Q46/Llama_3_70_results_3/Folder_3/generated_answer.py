from math import gcd
from functools import reduce

def gcf_three_nums(num_list):
    nums = [num_list[31], num_list[69], num_list[40]]
    return reduce(gcd, nums)