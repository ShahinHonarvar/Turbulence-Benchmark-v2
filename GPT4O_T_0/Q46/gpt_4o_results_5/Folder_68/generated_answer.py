import math

def gcf_three_nums(numbers):
    if len(numbers) < 8:
        return None
    return math.gcd(math.gcd(numbers[4], numbers[1]), numbers[7])