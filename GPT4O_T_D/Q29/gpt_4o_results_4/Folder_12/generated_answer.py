import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(56, 54):
        return None
    return math.gcd(numbers[56], numbers[54])