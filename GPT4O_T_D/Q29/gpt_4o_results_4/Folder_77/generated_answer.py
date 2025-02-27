import math

def gcf_two_nums(numbers):
    if len(numbers) < 842:
        return None
    return math.gcd(numbers[841], numbers[804])