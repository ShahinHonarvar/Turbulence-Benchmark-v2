import math

def gcf_three_nums(numbers):
    if len(numbers) < 93:
        return None
    return math.gcd(math.gcd(numbers[66], numbers[56]), numbers[92])