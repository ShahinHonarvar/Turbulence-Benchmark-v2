import math

def gcf_two_nums(numbers):
    if len(numbers) < 75:
        return None
    return math.gcd(numbers[29], numbers[74])