import math

def gcf_three_nums(numbers):
    if len(numbers) < 10:
        return None
    gcf = math.gcd(numbers[9], math.gcd(numbers[6], numbers[2]))
    return gcf