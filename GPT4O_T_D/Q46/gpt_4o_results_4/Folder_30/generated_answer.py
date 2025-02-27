import math

def gcf_three_nums(numbers):
    if len(numbers) < 77:
        raise ValueError('List must contain at least 77 elements.')
    a = numbers[76]
    b = numbers[35]
    c = numbers[74]
    return math.gcd(math.gcd(a, b), c)