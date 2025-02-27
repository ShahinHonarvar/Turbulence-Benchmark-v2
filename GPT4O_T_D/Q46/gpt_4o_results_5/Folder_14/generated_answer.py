from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    if len(numbers) >= 89:
        return reduce(gcd, (numbers[17], numbers[88], numbers[35]))
    return None