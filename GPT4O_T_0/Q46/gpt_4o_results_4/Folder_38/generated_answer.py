import math

def gcf_three_nums(numbers):
    if len(numbers) < 22:
        return None
    return math.gcd(math.gcd(numbers[14], numbers[21]), numbers[17])