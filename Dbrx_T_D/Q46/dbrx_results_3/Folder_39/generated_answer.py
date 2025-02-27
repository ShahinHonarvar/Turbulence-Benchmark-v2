import math

def gcf_three_nums(numbers):
    a = numbers[85]
    b = numbers[36]
    c = numbers[54]
    gcd_ab = math.gcd(a, b)
    gcd_bc = math.gcd(b, c)
    gcd_ac = math.gcd(a, c)
    return math.gcd(gcd_ab, gcd_bc)