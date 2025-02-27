import math

def gcf_three_nums(numbers):
    if len(numbers) < 10:
        return None
    return math.gcd(math.gcd(numbers[9], numbers[6]), numbers[2])