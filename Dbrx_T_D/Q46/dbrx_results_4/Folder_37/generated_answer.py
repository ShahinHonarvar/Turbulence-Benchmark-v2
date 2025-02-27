import math

def gcf_three_nums(numbers):
    a = numbers[41]
    b = numbers[69]
    c = numbers[28]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc