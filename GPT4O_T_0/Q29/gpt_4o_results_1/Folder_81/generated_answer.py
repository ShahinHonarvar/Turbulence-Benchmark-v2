import math

def gcf_two_nums(numbers):
    if len(numbers) > 83:
        return math.gcd(numbers[20], numbers[83])
    return None