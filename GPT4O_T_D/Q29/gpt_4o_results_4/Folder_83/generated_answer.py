from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) > 20:
        return gcd(numbers[17], numbers[20])
    return None