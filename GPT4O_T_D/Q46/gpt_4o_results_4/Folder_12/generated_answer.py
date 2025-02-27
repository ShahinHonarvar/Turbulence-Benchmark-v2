import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(91, 45, 48):
        return None
    return math.gcd(math.gcd(numbers[91], numbers[45]), numbers[48])