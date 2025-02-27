from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_numbers = [numbers[96], numbers[57], numbers[85]]
    return reduce(gcd, selected_numbers) if len(numbers) > max(96, 57, 85) else None