import math

def gcf_two_nums(numbers):
    if len(numbers) > 49:
        return math.gcd(numbers[28], numbers[49])
    return None