from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) < 54:
        return None
    selected_numbers = [numbers[53], numbers[23], numbers[45]]
    return reduce(gcd, selected_numbers)