import math

def gcf_three_nums(numbers):
    if len(numbers) < 77:
        return None
    return math.gcd(math.gcd(numbers[13], numbers[76]), numbers[44])