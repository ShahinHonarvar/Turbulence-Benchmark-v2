import math

def gcf_three_nums(numbers):
    if len(numbers) < 71:
        return None
    return math.gcd(math.gcd(numbers[13], numbers[70]), numbers[32])