import math

def gcf_three_nums(numbers):
    if len(numbers) < 96:
        raise ValueError('List must contain at least 96 elements.')
    a, b, c = (numbers[90], numbers[41], numbers[95])
    return math.gcd(math.gcd(a, b), c)