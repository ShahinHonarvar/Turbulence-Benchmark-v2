import math

def gcf_three_nums(numbers):
    a = numbers[13]
    b = numbers[76]
    c = numbers[44]
    gcd_a_b = math.gcd(a, b)
    gcd_ab_c = math.gcd(gcd_a_b, c)
    return gcd_ab_c