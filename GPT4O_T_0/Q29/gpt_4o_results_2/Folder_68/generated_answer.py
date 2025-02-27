import math

def gcf_two_nums(numbers):
    if len(numbers) < 10:
        return None
    return math.gcd(numbers[8], numbers[9])