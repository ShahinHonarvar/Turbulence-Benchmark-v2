import math

def gcf_three_nums(numbers):
    if len(numbers) < 75:
        raise ValueError('List must contain at least 75 integers.')
    a = numbers[29]
    b = numbers[74]
    c = numbers[49]
    return math.gcd(math.gcd(a, b), c)