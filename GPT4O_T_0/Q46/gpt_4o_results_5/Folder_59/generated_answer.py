import math

def gcf_three_nums(numbers):
    if len(numbers) < 9:
        return None
    return math.gcd(math.gcd(numbers[6], numbers[7]), numbers[8])