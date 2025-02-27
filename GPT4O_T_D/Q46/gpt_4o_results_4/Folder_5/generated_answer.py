import math

def gcf_three_nums(numbers):
    if len(numbers) < 81:
        return None
    a, b, c = (numbers[64], numbers[80], numbers[15])
    return math.gcd(math.gcd(a, b), c)