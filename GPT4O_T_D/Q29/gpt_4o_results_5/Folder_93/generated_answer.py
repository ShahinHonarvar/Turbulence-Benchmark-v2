import math

def gcf_two_nums(numbers):
    if len(numbers) > max(78, 16):
        return math.gcd(numbers[78], numbers[16])
    else:
        raise IndexError('Index out of range')