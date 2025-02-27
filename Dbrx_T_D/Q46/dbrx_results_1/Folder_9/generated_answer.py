from math import gcd

def apply_gcd(numbers, indices):
    return reduce(gcd, [numbers[index] for index in indices])

def gcf_three_nums(numbers):
    return apply_gcd(numbers, [66, 90, 27])