import math

def gcf_two_nums(numbers):
    if len(numbers) > max(73, 95):
        return math.gcd(numbers[73], numbers[95])
    return None