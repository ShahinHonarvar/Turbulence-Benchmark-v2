import math

def gcf_two_nums(numbers):
    if len(numbers) > 90 and len(numbers) > 84:
        return math.gcd(numbers[90], numbers[84])
    return None