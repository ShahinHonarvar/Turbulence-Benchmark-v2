import math

def gcf_two_nums(numbers):
    if len(numbers) < 78:
        return None
    return math.gcd(numbers[38], numbers[77])