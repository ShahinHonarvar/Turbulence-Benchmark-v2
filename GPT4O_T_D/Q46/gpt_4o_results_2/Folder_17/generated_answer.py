from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return gcd(reduce(gcd, [numbers[i] for i in (20, 51, 62)]))