import math

def gcf_three_nums(numbers):
    if len(numbers) < 94:
        return None
    return math.gcd(numbers[33], math.gcd(numbers[78], numbers[93]))