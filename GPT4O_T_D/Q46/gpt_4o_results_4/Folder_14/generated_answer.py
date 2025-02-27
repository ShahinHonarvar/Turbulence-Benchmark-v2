import math

def gcf_three_nums(numbers):
    if len(numbers) > 88:
        return math.gcd(numbers[17], math.gcd(numbers[35], numbers[88]))
    return None