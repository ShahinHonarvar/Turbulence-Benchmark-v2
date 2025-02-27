import math

def gcf_three_nums(numbers):
    if len(numbers) < 81:
        raise ValueError('List must contain at least 81 elements.')
    a = numbers[31]
    b = numbers[25]
    c = numbers[80]
    return math.gcd(math.gcd(a, b), c)