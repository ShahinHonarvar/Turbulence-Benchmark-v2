import math

def gcf_two_nums(numbers):
    if len(numbers) < 96:
        return None
    return math.gcd(numbers[87], numbers[95])