from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_numbers = [numbers[20], numbers[17], numbers[28]]
    return reduce(gcd, selected_numbers)