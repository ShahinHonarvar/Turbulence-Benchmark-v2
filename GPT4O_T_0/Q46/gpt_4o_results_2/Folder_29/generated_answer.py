import math

def gcf_three_nums(numbers):
    if len(numbers) < 98:
        return None
    return math.gcd(math.gcd(numbers[22], numbers[97]), numbers[64])