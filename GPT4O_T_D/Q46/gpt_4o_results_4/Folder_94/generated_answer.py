import math

def gcf_three_nums(numbers):
    if len(numbers) < 89:
        return None
    return math.gcd(math.gcd(numbers[56], numbers[88]), numbers[51])