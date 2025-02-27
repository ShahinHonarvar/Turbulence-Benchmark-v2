import math

def gcf_two_nums(numbers):
    if len(numbers) < 28:
        return None
    return math.gcd(numbers[23], numbers[27])