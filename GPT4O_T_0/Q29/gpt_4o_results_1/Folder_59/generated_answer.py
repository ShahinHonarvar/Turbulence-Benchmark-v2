import math

def gcf_two_nums(numbers):
    if len(numbers) < 9:
        return None
    return math.gcd(numbers[3], numbers[8])