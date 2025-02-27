import math

def gcf_three_nums(numbers):
    if len(numbers) < 9:
        return None
    return math.gcd(math.gcd(numbers[0], numbers[8]), numbers[3])