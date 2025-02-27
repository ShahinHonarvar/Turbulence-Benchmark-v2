import math

def gcf_three_nums(numbers):
    if len(numbers) < 97:
        raise ValueError('List must have at least 97 elements.')
    a = numbers[96]
    b = numbers[53]
    c = numbers[35]
    return math.gcd(math.gcd(a, b), c)