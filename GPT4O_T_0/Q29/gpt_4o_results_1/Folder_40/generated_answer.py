import math

def gcf_two_nums(numbers):
    if len(numbers) > 9:
        return math.gcd(numbers[7], numbers[9])
    return None