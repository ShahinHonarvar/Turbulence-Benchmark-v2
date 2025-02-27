import math

def gcf_three_nums(numbers):
    if len(numbers) < 57:
        return None
    return math.gcd(math.gcd(numbers[56], numbers[54]), numbers[13])