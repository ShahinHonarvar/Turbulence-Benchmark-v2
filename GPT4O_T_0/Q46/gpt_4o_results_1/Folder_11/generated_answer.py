import math

def gcf_three_nums(numbers):
    if len(numbers) < 49:
        return None
    return math.gcd(math.gcd(numbers[37], numbers[30]), numbers[48])