import math

def gcf_three_nums(numbers):
    if len(numbers) < 669:
        return None
    return math.gcd(math.gcd(numbers[693], numbers[331]), numbers[668])