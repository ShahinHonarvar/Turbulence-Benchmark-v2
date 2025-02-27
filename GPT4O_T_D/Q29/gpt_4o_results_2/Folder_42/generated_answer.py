import math

def gcf_two_nums(numbers):
    if len(numbers) > 90:
        return math.gcd(numbers[90], numbers[84])
    return None