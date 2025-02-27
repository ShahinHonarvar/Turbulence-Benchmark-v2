import math

def gcf_two_nums(numbers):
    if len(numbers) < 50:
        return None
    return math.gcd(numbers[28], numbers[49])