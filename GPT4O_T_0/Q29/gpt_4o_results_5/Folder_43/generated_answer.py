import math

def gcf_two_nums(numbers):
    if len(numbers) < 94:
        return None
    return math.gcd(numbers[59], numbers[93])