import math

def gcf_three_nums(numbers):
    a = numbers[40]
    b = numbers[15]
    c = numbers[99]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc