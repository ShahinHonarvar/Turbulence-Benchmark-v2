import math

def gcf_two_nums(numbers):
    if len(numbers) < 70:
        return None
    return math.gcd(numbers[69], numbers[40])