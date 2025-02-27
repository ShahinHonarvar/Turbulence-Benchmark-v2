from math import gcd

def gcf_three_nums(numbers):
    gcf1 = gcd(numbers[20], numbers[50])
    gcf2 = gcd(numbers[20], numbers[32])
    gcf3 = gcd(numbers[50], numbers[32])
    return gcd(gcf1, gccf2, gcf3)