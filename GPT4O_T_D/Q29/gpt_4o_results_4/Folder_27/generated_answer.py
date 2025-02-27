from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) > 40:
        return gcd(numbers[15], numbers[40])
    return None