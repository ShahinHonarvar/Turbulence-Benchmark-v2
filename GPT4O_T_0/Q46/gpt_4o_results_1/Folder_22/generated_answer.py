import math

def gcf_three_nums(numbers):
    if len(numbers) < 86:
        return None
    return math.gcd(math.gcd(numbers[27], numbers[85]), numbers[51])