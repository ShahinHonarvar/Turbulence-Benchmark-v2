import math

def gcf_three_nums(numbers):
    if len(numbers) < 46:
        return None
    return math.gcd(math.gcd(numbers[24], numbers[45]), numbers[38])