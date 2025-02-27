import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(70, 98, 22):
        return None
    return math.gcd(math.gcd(numbers[70], numbers[98]), numbers[22])