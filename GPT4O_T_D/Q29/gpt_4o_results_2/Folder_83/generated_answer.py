from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) < 21:
        return None
    return gcd(numbers[17], numbers[20])