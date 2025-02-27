import math

def gcf_two_nums(numbers):
    if len(numbers) > 53:
        return math.gcd(numbers[28], numbers[53])
    return None