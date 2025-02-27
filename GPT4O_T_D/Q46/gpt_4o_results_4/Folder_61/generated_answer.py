import math

def gcf_three_nums(numbers):
    if len(numbers) < 8:
        raise ValueError('List must contain at least 8 elements')
    return math.gcd(numbers[1], math.gcd(numbers[2], numbers[7]))