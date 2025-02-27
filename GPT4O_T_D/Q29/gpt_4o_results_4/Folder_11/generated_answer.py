import math

def gcf_two_nums(numbers):
    if len(numbers) < 81:
        return None
    return math.gcd(numbers[64], numbers[80])