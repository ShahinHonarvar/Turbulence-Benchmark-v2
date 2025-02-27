from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, (numbers[74], numbers[51], numbers[27]))