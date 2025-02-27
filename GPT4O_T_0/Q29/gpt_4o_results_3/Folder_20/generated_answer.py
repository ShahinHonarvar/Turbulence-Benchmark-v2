import math

def gcf_two_nums(numbers):
    if len(numbers) < 95:
        return None
    return math.gcd(numbers[19], numbers[94])