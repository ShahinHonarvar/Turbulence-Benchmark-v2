import math

def gcf_three_nums(numbers):
    if len(numbers) < 75:
        return None
    return math.gcd(numbers[29], math.gcd(numbers[74], numbers[49]))