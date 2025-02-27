from math import gcd

def gcf_three_nums(numbers):
    a, b, c = (numbers[0], numbers[8], numbers[3])
    return gcd(a, gcd(b, c))