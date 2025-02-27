import math

def gcf_three_nums(numbers):
    if len(numbers) < 96:
        return None
    return math.gcd(math.gcd(numbers[20], numbers[43]), numbers[95])