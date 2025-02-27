import math

def gcf_two_nums(numbers):
    if len(numbers) > 66:
        return math.gcd(numbers[13], numbers[66])
    return None