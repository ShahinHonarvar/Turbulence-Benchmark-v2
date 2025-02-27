import math

def gcf_two_nums(numbers):
    if len(numbers) < 313:
        raise ValueError('The list must contain at least 313 numbers.')
    return math.gcd(numbers[180], numbers[312])