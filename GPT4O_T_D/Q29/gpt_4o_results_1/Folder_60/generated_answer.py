import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(28, 53):
        return None
    return math.gcd(numbers[28], numbers[53])