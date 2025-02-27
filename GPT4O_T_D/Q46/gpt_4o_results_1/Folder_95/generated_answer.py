import math

def gcf_three_nums(numbers):
    if len(numbers) < 88:
        raise ValueError('List must contain at least 88 elements.')
    return math.gcd(math.gcd(numbers[87], numbers[20]), numbers[36])