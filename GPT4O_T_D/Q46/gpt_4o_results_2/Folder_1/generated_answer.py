import math

def gcf_three_nums(numbers):
    if len(numbers) < 75:
        return None
    return math.gcd(math.gcd(numbers[74], numbers[51]), numbers[27])