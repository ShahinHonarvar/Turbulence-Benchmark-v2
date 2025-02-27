import math

def gcf_three_nums(numbers):
    a = numbers[96]
    b = numbers[57]
    c = numbers[85]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc