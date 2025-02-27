import math

def gcf_three_nums(numbers):
    if len(numbers) < 55:
        return None
    return math.gcd(math.gcd(numbers[32], numbers[54]), numbers[13])