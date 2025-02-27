import math

def gcf_two_nums(numbers):
    if len(numbers) > 99:
        return math.gcd(numbers[15], numbers[99])
    return None