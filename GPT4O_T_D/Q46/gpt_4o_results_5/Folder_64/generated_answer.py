from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    indices = [0, 8, 3]
    return reduce(gcd, (numbers[i] for i in indices if i < len(numbers)))