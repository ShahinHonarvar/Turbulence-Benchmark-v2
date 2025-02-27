import math

def gcf_three_nums(numbers):
    if len(numbers) < 56:
        return None
    return math.gcd(math.gcd(numbers[10], numbers[55]), numbers[36])