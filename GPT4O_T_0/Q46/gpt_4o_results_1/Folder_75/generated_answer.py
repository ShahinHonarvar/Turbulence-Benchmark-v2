import math

def gcf_three_nums(numbers):
    if len(numbers) < 99:
        return None
    return math.gcd(math.gcd(numbers[70], numbers[98]), numbers[22])