from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[i] for i in [21, 51, 33]])