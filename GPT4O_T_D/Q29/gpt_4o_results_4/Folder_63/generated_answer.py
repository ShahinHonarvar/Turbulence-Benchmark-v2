import math

def gcf_two_nums(numbers):
    if len(numbers) > 21 and len(numbers) > 17:
        return math.gcd(numbers[21], numbers[17])
    return None