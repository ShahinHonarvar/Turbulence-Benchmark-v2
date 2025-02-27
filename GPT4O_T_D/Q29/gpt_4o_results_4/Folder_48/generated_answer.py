import math

def gcf_two_nums(numbers):
    if len(numbers) > max(618, 195):
        return math.gcd(numbers[618], numbers[195])
    else:
        raise IndexError('List does not contain enough elements.')