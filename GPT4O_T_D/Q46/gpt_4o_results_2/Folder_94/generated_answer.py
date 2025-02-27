import math

def gcf_three_nums(numbers):
    if len(numbers) < 89:
        raise ValueError('List must contain at least 89 elements.')
    a = numbers[56]
    b = numbers[88]
    c = numbers[51]
    return math.gcd(math.gcd(a, b), c)