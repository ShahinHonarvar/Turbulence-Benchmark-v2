from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return gcd(lst[44], gcd(lst[91], lst[42]))