import math

def gcf_three_nums(numbers):
    a = numbers[20]
    b = numbers[43]
    c = numbers[95]
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc