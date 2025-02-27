from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    if len(lst) <= max(34, 38, 77):
        return None
    numbers = [lst[34], lst[38], lst[77]]
    return reduce(gcd, numbers)