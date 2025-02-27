import math

def gcf_two_nums(numbers):
    if len(numbers) > max(83, 14):
        return math.gcd(numbers[83], numbers[14])
    return None