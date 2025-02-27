import math

def gcf_three_nums(numbers):
    a = numbers[36]
    b = numbers[85]
    c = numbers[83]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)