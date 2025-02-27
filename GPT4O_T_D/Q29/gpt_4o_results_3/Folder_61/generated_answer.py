import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(8, 3):
        return None
    return math.gcd(numbers[8], numbers[3])