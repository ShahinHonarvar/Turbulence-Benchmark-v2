import math

def gcf_three_nums(numbers):
    if len(numbers) < 77:
        return None
    return math.gcd(math.gcd(numbers[15], numbers[51]), numbers[76])