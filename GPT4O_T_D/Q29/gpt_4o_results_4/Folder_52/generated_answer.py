import math

def gcf_two_nums(numbers):
    if len(numbers) > 90 and len(numbers) > 41:
        return math.gcd(numbers[90], numbers[41])
    return None