import math

def gcf_three_nums(numbers):
    if len(numbers) < 10:
        return None
    return math.gcd(math.gcd(numbers[0], numbers[7]), numbers[9])