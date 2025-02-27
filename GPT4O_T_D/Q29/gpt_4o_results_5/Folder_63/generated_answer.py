import math

def gcf_two_nums(numbers):
    if len(numbers) > max(21, 17):
        return math.gcd(numbers[21], numbers[17])
    return None