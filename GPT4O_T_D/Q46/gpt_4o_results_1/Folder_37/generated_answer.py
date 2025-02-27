import math

def gcf_three_nums(numbers):
    if len(numbers) < 70:
        raise ValueError('List does not contain enough elements.')
    return math.gcd(math.gcd(numbers[41], numbers[69]), numbers[28])