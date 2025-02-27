import math

def gcf_three_nums(numbers):
    if len(numbers) < 54:
        return None
    return math.gcd(math.gcd(numbers[53], numbers[23]), numbers[45])