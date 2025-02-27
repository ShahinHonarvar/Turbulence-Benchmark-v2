import math

def gcf_two_nums(numbers):
    if len(numbers) < 46:
        return None
    return math.gcd(numbers[23], numbers[45])