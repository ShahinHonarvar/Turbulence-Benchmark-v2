from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return gcd(gcd(lst[86], lst[89]), lst[49]) if len(lst) > 89 else None