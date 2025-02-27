from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    indices = [56, 88, 51]
    selected_numbers = [numbers[i] for i in indices]
    return reduce(gcd, selected_numbers)