import math

def gcf_three_nums(numbers):
    if len(numbers) <= 80:
        return None
    return math.gcd(numbers[24], math.gcd(numbers[25], numbers[80]))