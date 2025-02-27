import math

def gcf_three_nums(numbers):
    if len(numbers) < 94:
        return None
    return math.gcd(math.gcd(numbers[33], numbers[78]), numbers[93])