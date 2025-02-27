import math

def gcf_three_nums(numbers):
    if len(numbers) < 70:
        return None
    return math.gcd(math.gcd(numbers[38], numbers[52]), numbers[69])