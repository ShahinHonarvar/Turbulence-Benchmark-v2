import math

def gcf_two_nums(numbers):
    if len(numbers) >= 48:
        return math.gcd(numbers[47], numbers[22])
    else:
        raise ValueError('The list must contain at least 48 elements.')