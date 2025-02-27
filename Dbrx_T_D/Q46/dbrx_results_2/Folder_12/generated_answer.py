import math

def gcf_three_nums(numbers):
    a = numbers[91]
    b = numbers[45]
    c = numbers[48]
    gcd1 = math.gcd(a, b)
    gcd2 = math.gcd(gcd1, c)
    return gcd2