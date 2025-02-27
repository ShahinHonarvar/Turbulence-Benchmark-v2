import math

def gcf_two_nums(numbers):
    if len(numbers) < 91:
        return None
    return math.gcd(numbers[90], numbers[84])