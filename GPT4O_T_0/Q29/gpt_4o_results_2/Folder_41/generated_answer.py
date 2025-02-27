import math

def gcf_two_nums(numbers):
    if len(numbers) > 27:
        return math.gcd(numbers[23], numbers[27])
    return None