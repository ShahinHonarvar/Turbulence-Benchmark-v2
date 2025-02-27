import math

def gcf_three_nums(numbers):
    if len(numbers) < 97:
        return None
    return math.gcd(math.gcd(numbers[96], numbers[53]), numbers[35])