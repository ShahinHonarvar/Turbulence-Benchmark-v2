from math import gcd

def gcf_three_nums(numbers):
    return gcd(numbers[1], gcd(numbers[2], numbers[7]))