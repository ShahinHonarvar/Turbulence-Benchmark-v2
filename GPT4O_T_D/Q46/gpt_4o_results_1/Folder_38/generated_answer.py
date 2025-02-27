import math

def gcf_three_nums(numbers):
    if len(numbers) > 21:
        return math.gcd(math.gcd(numbers[14], numbers[21]), numbers[17])
    return None