import math

def gcf_two_nums(numbers):
    if len(numbers) <= 28 or len(numbers) <= 20:
        return None
    return math.gcd(numbers[28], numbers[20])