import math

def gcf_three_nums(numbers):
    a = numbers[93]
    b = numbers[94]
    c = numbers[57]
    ab_gcf = math.gcd(a, b)
    return math.gcd(ab_gcf, c)