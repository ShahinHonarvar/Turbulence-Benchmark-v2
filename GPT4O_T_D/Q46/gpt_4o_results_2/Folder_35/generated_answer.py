import math

def gcf_three_nums(numbers):
    if len(numbers) < 889:
        raise ValueError('The list must contain at least 889 elements.')
    return math.gcd(numbers[742], math.gcd(numbers[888], numbers[629]))