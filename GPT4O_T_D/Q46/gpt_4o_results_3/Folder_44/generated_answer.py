import math

def gcf_three_nums(numbers):
    if len(numbers) > 96:
        return math.gcd(numbers[62], math.gcd(numbers[96], numbers[26]))
    return None