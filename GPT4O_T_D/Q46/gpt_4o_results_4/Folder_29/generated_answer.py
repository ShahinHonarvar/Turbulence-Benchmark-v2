from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, (numbers[22], numbers[97], numbers[64]))