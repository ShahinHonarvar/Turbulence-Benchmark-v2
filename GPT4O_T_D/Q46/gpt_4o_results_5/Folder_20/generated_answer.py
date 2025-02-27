from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    indices = [29, 53, 42]
    selected_values = [numbers[i] for i in indices]
    return reduce(gcd, selected_values)