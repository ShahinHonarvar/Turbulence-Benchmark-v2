import math

def gcf_two_nums(numbers):
    if len(numbers) >= 1:
        return math.gcd(numbers[0], numbers[0])
    return None