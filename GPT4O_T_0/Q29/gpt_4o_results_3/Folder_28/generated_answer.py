import math

def gcf_two_nums(numbers):
    if len(numbers) > 76:
        return math.gcd(numbers[48], numbers[76])
    return None