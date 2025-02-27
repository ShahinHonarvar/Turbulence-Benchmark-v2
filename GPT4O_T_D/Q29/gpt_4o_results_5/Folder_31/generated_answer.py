import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(87, 95):
        return None
    return math.gcd(numbers[87], numbers[95])