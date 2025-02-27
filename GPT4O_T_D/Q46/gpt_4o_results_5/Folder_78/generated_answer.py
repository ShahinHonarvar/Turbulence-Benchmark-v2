import math

def gcf_three_nums(numbers):
    if len(numbers) > 70:
        return math.gcd(numbers[13], math.gcd(numbers[70], numbers[32]))
    return None