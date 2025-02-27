import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(46, 84):
        return None
    return math.gcd(numbers[46], numbers[84])