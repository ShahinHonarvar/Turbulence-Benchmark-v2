import math

def gcf_three_nums(numbers):
    if len(numbers) < 835:
        return None
    return math.gcd(math.gcd(numbers[404], numbers[834]), numbers[517])