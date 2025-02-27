import math

def gcf_three_nums(numbers):
    if len(numbers) < 94:
        raise ValueError('List must have at least 94 elements')
    return math.gcd(math.gcd(numbers[59], numbers[84]), numbers[93])