import math

def gcf_three_nums(numbers):
    if len(numbers) < 70:
        raise ValueError('The list must contain at least 70 elements.')
    a = numbers[38]
    b = numbers[52]
    c = numbers[69]
    return math.gcd(math.gcd(a, b), c)