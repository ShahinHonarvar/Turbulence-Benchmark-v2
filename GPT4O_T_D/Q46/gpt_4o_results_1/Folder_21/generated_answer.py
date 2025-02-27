import math

def gcf_three_nums(numbers):
    if len(numbers) < 933:
        return None
    return math.gcd(numbers[412], math.gcd(numbers[932], numbers[337]))