import math

def gcf_three_nums(numbers):
    if len(numbers) < 91:
        raise ValueError('List must have at least 91 elements.')
    return math.gcd(math.gcd(numbers[66], numbers[90]), numbers[27])