from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    values = [numbers[31], numbers[25], numbers[80]]
    return reduce(gcd, values)