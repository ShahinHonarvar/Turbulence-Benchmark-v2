import math

def gcf_two_nums(numbers):
    if len(numbers) > 20:
        return math.gcd(numbers[17], numbers[20])
    else:
        return None