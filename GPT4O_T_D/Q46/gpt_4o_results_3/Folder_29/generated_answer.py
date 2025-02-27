import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(22, 64, 97):
        return None
    a = numbers[22]
    b = numbers[97]
    c = numbers[64]
    return math.gcd(math.gcd(a, b), c)