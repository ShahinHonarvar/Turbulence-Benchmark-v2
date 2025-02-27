import math

def gcf_two_nums(numbers):
    if len(numbers) > 80:
        return math.gcd(numbers[25], numbers[80])
    return None