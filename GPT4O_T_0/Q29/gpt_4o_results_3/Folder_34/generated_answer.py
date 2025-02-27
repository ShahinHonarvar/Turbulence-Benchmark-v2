import math

def gcf_two_nums(numbers):
    if len(numbers) > 64:
        return math.gcd(numbers[60], numbers[64])
    return None