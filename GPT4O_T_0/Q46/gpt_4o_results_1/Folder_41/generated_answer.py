import math

def gcf_three_nums(numbers):
    if len(numbers) < 95:
        return None
    return math.gcd(math.gcd(numbers[19], numbers[94]), numbers[78])