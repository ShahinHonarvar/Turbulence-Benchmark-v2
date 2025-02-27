from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) > 49:
        return gcd(numbers[49], numbers[31])
    return None