import math

def gcf_three_nums(numbers):
    if len(numbers) < 85:
        return None
    return math.gcd(numbers[67], math.gcd(numbers[84], numbers[13]))