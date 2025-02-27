import math

def gcf_three_nums(numbers):
    if len(numbers) < 54:
        raise ValueError('List must contain at least 54 elements')
    a, b, c = (numbers[29], numbers[53], numbers[42])
    return math.gcd(math.gcd(a, b), c)