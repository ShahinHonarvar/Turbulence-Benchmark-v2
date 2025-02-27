import math

def gcf_three_nums(numbers):
    if len(numbers) >= 9:
        return math.gcd(math.gcd(numbers[4], numbers[0]), numbers[8])
    return None