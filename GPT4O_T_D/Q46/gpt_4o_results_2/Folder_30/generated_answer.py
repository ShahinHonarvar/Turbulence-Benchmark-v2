import math

def gcf_three_nums(numbers):
    if len(numbers) < 75:
        raise ValueError('List must contain at least 75 elements')
    return math.gcd(numbers[76], math.gcd(numbers[35], numbers[74]))