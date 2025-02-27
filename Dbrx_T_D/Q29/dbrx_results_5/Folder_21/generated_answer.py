from gcd import gcd
from functools import reduce

def gcf_two_nums(numbers):
    return reduce(gcd, (numbers[198], numbers[212]))