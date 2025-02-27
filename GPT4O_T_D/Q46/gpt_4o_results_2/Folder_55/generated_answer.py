import math

def gcf_three_nums(numbers):
    if len(numbers) < 10:
        raise ValueError('The list must contain at least 10 numbers.')
    return math.gcd(math.gcd(numbers[9], numbers[6]), numbers[2])