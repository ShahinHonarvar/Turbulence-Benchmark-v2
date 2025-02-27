import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(24, 45, 38):
        return None
    return math.gcd(numbers[24], math.gcd(numbers[45], numbers[38]))