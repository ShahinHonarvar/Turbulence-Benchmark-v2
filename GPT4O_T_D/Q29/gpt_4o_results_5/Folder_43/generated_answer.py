import math

def gcf_two_nums(numbers):
    if len(numbers) < 94:
        raise ValueError('List must contain at least 94 elements')
    return math.gcd(numbers[59], numbers[93])