import math

def gcf_three_nums(numbers):
    if len(numbers) < 75:
        return None
    return math.gcd(math.gcd(numbers[19], numbers[49]), numbers[74])