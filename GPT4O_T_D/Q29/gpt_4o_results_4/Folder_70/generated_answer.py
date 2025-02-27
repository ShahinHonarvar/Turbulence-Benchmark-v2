import math

def gcf_two_nums(numbers):
    if len(numbers) > 616:
        return math.gcd(numbers[300], numbers[616])
    else:
        return None