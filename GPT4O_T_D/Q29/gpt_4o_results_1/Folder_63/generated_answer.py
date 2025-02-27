import math

def gcf_two_nums(numbers):
    if len(numbers) < 22:
        return None
    return math.gcd(numbers[21], numbers[17])