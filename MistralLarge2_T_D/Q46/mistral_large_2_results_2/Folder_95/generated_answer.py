from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[87], lst[20], lst[36]])