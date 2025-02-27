from math import gcd

def gcf_three_nums(numbers):
    a = numbers[21]
    b = numbers[69]
    c = numbers[41]
    return gcd(gcd(a, b), c)