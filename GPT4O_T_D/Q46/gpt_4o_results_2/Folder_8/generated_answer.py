import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(99, 28, 53):
        raise ValueError('List must contain at least 100 elements.')
    return math.gcd(numbers[99], math.gcd(numbers[28], numbers[53]))