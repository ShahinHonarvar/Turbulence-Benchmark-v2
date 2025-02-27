from math import gcd

def apply_gcd(x, y):
    return gcd(x, y)

def gcf_three_nums(numbers):
    elements = [numbers[96], numbers[53], numbers[35]]
    return reduce(apply_gcd, elements)