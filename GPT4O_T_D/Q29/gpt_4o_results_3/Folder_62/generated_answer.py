import math

def gcf_two_nums(numbers):
    if len(numbers) > 51:
        return math.gcd(numbers[51], numbers[31])
    return None