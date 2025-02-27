import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(64, 80):
        return None
    return math.gcd(numbers[64], numbers[80])