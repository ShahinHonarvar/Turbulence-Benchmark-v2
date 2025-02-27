import math

def gcf_three_nums(numbers):
    if len(numbers) < 91:
        return None
    return math.gcd(math.gcd(numbers[90], numbers[84]), numbers[47])