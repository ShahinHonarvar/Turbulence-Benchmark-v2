import math

def gcf_three_nums(numbers):
    a = numbers[22]
    b = numbers[97]
    c = numbers[64]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc