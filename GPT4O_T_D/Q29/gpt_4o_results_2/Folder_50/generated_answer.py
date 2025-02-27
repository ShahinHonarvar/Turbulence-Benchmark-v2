import math

def gcf_two_nums(numbers):
    if len(numbers) < 91:
        raise ValueError('List must contain at least 91 elements')
    return math.gcd(numbers[90], numbers[54])