from functools import reduce

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_two_nums(numbers):
    numerator = numbers[6]
    denominator = numbers[9]
    return gcd(numerator, denominator)