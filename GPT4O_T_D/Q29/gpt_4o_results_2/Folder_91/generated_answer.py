import math

def gcf_two_nums(numbers):
    if len(numbers) < 5:
        return None
    return math.gcd(numbers[0], numbers[4])