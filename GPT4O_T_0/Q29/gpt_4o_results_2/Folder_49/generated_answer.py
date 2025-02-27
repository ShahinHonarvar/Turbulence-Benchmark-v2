import math

def gcf_two_nums(numbers):
    if len(numbers) > 28:
        return math.gcd(numbers[28], numbers[20])
    return None