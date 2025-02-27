import math

def gcf_two_nums(numbers):
    if len(numbers) < 85:
        return None
    return math.gcd(numbers[46], numbers[84])