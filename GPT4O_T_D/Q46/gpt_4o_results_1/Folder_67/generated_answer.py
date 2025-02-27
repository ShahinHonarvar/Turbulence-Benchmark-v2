import math

def gcf_three_nums(numbers):
    if len(numbers) < 71:
        raise ValueError('List must have at least 71 elements')
    return math.gcd(math.gcd(numbers[70], numbers[41]), numbers[20])