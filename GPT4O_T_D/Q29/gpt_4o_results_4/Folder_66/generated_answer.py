import math

def gcf_two_nums(numbers):
    if len(numbers) < 90:
        return None
    return math.gcd(numbers[86], numbers[89])