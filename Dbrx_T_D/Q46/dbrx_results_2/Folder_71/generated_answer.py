import math

def gcf_three_nums(numbers):
    a = numbers[24]
    b = numbers[45]
    c = numbers[38]
    gcd_multiple = math.gcd(a, math.gcd(b, c))
    return gcd_multiple