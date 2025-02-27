import math

def gcf_three_nums(numbers):
    if len(numbers) < 100:
        return None
    return math.gcd(math.gcd(numbers[99], numbers[63]), numbers[74])