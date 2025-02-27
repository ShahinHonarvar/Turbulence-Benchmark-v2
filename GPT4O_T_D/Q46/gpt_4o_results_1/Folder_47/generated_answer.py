import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(36, 85, 83):
        raise ValueError('List must have at least 86 elements.')
    a = numbers[36]
    b = numbers[85]
    c = numbers[83]
    return math.gcd(math.gcd(a, b), c)