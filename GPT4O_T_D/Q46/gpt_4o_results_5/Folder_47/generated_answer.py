import math

def gcf_three_nums(numbers):
    if len(numbers) < 86:
        raise ValueError('List must contain at least 86 elements')
    return math.gcd(math.gcd(numbers[36], numbers[85]), numbers[83])