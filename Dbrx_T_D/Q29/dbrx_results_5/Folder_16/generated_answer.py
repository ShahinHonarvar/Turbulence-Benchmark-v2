import math

def gcf_two_nums(numbers):
    a = numbers[860]
    b = numbers[307]
    return math.gcd(a, b) if a < 1 or b < 1 else max(math.gcd(a, b), 1)