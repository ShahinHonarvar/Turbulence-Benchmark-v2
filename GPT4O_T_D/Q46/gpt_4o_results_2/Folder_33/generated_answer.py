import math

def gcf_three_nums(numbers):
    if len(numbers) < 565:
        return None
    return math.gcd(math.gcd(numbers[252], numbers[149]), numbers[564])