import math

def gcf_three_nums(numbers):
    if len(numbers) < 96:
        return None
    return math.gcd(math.gcd(numbers[16], numbers[87]), numbers[95])