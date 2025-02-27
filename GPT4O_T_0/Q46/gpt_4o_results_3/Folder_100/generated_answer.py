import math

def gcf_three_nums(numbers):
    if len(numbers) < 52:
        return None
    return math.gcd(math.gcd(numbers[21], numbers[51]), numbers[33])