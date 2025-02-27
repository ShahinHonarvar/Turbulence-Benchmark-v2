import math

def gcf_three_nums(numbers):
    a = numbers[307]
    b = numbers[920]
    c = numbers[463]
    gcd_ab = math.gcd(a, b)
    gcd_bc = math.gcd(b, c)
    gcd = math.gcd(gcd_ab, gcd_bc)
    return gcd