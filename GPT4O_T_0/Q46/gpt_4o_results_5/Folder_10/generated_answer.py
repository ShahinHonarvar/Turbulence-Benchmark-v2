import math

def gcf_three_nums(numbers):
    if len(numbers) < 90:
        return None
    return math.gcd(math.gcd(numbers[86], numbers[89]), numbers[49])