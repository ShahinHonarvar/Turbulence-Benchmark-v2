import math

def gcf_three_nums(numbers):
    a = numbers[53]
    b = numbers[23]
    c = numbers[45]
    gcf = math.gcd(a, math.gcd(b, c))
    return gcf