import math

def gcf_two_nums(numbers):
    if len(numbers) <= 90 or len(numbers) <= 54:
        return None
    return math.gcd(numbers[90], numbers[54])