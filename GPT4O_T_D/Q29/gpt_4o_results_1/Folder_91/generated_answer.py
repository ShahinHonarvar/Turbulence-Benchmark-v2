from math import gcd

def gcf_two_nums(numbers):
    return gcd(numbers[4], numbers[0]) if len(numbers) > 4 else None