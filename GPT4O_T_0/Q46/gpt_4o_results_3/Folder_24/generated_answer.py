import math

def gcf_three_nums(numbers):
    if len(numbers) < 44:
        return None
    return math.gcd(math.gcd(numbers[18], numbers[37]), numbers[43])