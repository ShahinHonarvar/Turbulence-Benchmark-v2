import math

def gcf_two_nums(numbers):
    if len(numbers) < 38:
        return None
    return math.gcd(numbers[37], numbers[30])