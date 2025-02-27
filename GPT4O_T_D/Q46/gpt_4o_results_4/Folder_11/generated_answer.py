from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    selected_numbers = [numbers[37], numbers[30], numbers[48]]
    return reduce(gcd, selected_numbers)