from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, (numbers[145], numbers[183], numbers[770]))