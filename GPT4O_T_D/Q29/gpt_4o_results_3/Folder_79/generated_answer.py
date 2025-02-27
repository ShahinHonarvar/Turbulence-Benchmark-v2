import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(85, 51):
        raise IndexError('The list must contain more than 85 elements.')
    return math.gcd(numbers[85], numbers[51])