import math

def gcf_two_nums(numbers):
    if len(numbers) > max(33, 72):
        return math.gcd(numbers[33], numbers[72])
    return None