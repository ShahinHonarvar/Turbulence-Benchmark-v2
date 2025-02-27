import math

def gcf_three_nums(numbers):
    if len(numbers) < 915:
        return None
    return math.gcd(math.gcd(numbers[695], numbers[710]), numbers[914])