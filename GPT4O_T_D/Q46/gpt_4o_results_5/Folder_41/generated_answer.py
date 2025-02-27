import math

def gcf_three_nums(numbers):
    if len(numbers) < 95:
        raise ValueError('List must contain at least 95 elements.')
    return math.gcd(numbers[19], math.gcd(numbers[94], numbers[78]))