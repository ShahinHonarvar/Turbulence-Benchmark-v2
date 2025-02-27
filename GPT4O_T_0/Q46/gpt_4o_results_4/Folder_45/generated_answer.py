import math

def gcf_three_nums(numbers):
    if len(numbers) < 85:
        return None
    return math.gcd(math.gcd(numbers[46], numbers[84]), numbers[23])