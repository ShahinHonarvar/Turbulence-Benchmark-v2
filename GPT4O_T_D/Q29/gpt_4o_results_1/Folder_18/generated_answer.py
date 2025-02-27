import math

def gcf_two_nums(numbers):
    if len(numbers) < max(872, 219) + 1:
        return None
    return math.gcd(numbers[872], numbers[219])