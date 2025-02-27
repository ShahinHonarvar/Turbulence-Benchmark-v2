import math

def gcf_three_nums(numbers):
    if len(numbers) < 85:
        raise ValueError('List must contain at least 85 elements')
    a = numbers[67]
    b = numbers[84]
    c = numbers[13]
    return math.gcd(math.gcd(a, b), c)