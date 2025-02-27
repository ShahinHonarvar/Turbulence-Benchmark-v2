import math

def gcf_three_nums(numbers):
    if len(numbers) < 48:
        return None
    return math.gcd(math.gcd(numbers[47], numbers[10]), numbers[28])