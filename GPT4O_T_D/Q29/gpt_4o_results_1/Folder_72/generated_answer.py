import math

def gcf_two_nums(numbers):
    if len(numbers) > 37:
        return math.gcd(numbers[18], numbers[37])
    else:
        return None