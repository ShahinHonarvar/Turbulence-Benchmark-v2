import math

def gcf_three_nums(numbers):
    if len(numbers) > 93:
        return math.gcd(numbers[59], math.gcd(numbers[93], numbers[84]))
    return None