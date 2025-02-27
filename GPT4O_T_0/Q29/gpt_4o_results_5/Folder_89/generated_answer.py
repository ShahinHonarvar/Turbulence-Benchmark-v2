import math

def gcf_two_nums(numbers):
    if len(numbers) > 37 and len(numbers) > 30:
        return math.gcd(numbers[37], numbers[30])
    return None