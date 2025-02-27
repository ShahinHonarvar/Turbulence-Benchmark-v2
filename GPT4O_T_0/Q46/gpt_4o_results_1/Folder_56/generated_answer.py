import math

def gcf_three_nums(numbers):
    if len(numbers) < 94:
        return None
    return math.gcd(math.gcd(numbers[59], numbers[93]), numbers[84])