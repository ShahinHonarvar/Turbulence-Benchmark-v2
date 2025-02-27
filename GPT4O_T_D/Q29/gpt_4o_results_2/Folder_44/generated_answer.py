import math

def gcf_two_nums(numbers):
    if len(numbers) < 89:
        return None
    return math.gcd(numbers[56], numbers[88])