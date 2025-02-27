import math

def gcf_two_nums(numbers):
    if len(numbers) > 94:
        return math.gcd(numbers[19], numbers[94])
    return None