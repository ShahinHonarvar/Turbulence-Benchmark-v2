from functools import reduce

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_two_nums(numbers):
    numbers_64_80 = [numbers[64], numbers[80]]
    gcf = reduce(lambda x, y: gcd(x, y), numbers_64_80)
    return gcf