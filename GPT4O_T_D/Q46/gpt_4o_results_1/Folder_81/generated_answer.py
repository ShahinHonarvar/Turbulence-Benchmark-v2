import math

def gcf_three_nums(numbers):
    if len(numbers) < 29:
        return None
    a = numbers[20]
    b = numbers[17]
    c = numbers[28]
    return math.gcd(math.gcd(a, b), c)