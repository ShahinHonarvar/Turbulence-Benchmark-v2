import math

def gcf_two_nums(numbers):
    if len(numbers) > 89:
        return math.gcd(numbers[86], numbers[89])
    return None