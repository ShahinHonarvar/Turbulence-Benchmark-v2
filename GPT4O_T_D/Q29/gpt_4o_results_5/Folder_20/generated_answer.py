import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(19, 94):
        return None
    return math.gcd(numbers[19], numbers[94])