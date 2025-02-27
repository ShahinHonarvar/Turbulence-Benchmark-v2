import math

def gcf_three_nums(numbers):
    if len(numbers) < 85:
        return None
    return math.gcd(numbers[85], math.gcd(numbers[36], numbers[54]))