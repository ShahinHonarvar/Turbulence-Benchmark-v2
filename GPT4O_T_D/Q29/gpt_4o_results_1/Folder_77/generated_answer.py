import math

def gcf_two_nums(numbers):
    if len(numbers) <= max(841, 804):
        return None
    return math.gcd(numbers[841], numbers[804])