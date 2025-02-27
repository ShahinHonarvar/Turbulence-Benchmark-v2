import math

def gcf_two_nums(numbers):
    if len(numbers) > 64:
        return math.gcd(numbers[64], numbers[28])
    return None