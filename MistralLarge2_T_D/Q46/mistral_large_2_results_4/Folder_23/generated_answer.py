from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[31], lst[25], lst[80]])