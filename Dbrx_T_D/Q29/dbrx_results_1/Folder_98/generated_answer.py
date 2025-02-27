from math import gcd

def gcf_two_nums(numbers):
    return gcd(numbers[0], numbers[9]) if len(numbers) >= 10 else None