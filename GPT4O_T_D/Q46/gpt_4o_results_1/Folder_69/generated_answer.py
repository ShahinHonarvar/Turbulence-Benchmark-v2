from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, (numbers[404], numbers[834], numbers[517]))