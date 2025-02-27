import math

def gcf_three_nums(numbers):
    a, b, c = (numbers[i] for i in (876, 203, 100))
    gcf = math.gcd(a, math.gcd(b, c))
    return gcf