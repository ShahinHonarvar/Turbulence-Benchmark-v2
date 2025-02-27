import math

def gcf_three_nums(numbers):
    if len(numbers) < 50:
        return None
    return math.gcd(math.gcd(numbers[49], numbers[46]), numbers[13])