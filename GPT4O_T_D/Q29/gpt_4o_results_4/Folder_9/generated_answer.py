import math

def gcf_two_nums(numbers):
    if len(numbers) >= 85:
        return math.gcd(numbers[84], numbers[63])
    return None