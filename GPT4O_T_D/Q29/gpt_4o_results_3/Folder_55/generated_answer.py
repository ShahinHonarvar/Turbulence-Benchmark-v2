import math

def gcf_two_nums(numbers):
    if len(numbers) < 3:
        return None
    return math.gcd(numbers[2], numbers[1])