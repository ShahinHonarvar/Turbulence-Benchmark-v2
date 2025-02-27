from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) > 28:
        return gcd(numbers[28], numbers[17])
    return None