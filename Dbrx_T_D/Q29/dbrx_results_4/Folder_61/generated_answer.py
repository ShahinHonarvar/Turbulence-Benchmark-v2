from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) < 10:
        return -1
    return gcd(numbers[8], numbers[3])