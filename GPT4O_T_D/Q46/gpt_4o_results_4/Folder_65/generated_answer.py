from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 77:
        raise ValueError('List must contain at least 77 elements.')
    relevant_numbers = [numbers[18], numbers[10], numbers[76]]
    return reduce(gcd, relevant_numbers)