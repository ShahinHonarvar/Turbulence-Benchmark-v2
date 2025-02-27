import math

def gcf_two_nums(numbers):
    if len(numbers) > 47 and len(numbers) > 10:
        return math.gcd(numbers[47], numbers[10])
    return None