import math

def gcf_three_nums(numbers):
    if len(numbers) < 629:
        raise ValueError('List must contain at least 629 elements.')
    return math.gcd(math.gcd(numbers[558], numbers[110]), numbers[628])