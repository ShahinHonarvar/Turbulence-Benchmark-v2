import math

def gcf_three_nums(numbers):
    a = numbers[25]
    b = numbers[76]
    c = numbers[57]
    factor = math.gcd(a, b)
    return math.gcd(factor, c)