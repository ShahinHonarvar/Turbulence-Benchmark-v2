import math

def gcf_three_nums(numbers):
    if len(numbers) <= 80:
        return None
    return math.gcd(math.gcd(numbers[24], numbers[25]), numbers[80])