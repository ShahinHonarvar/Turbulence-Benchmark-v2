import math

def gcf_three_nums(numbers):
    if len(numbers) > max(991, 244, 974):
        a = numbers[991]
        b = numbers[244]
        c = numbers[974]
        return math.gcd(math.gcd(a, b), c)
    return None