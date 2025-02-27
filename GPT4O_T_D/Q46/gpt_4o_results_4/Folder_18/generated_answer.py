import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(637, 411, 757):
        raise ValueError('List does not contain enough elements.')
    return math.gcd(numbers[637], math.gcd(numbers[411], numbers[757]))