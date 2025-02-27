import math

def gcf_three_nums(numbers):
    if len(numbers) > 99:
        a, b, c = (numbers[99], numbers[95], numbers[80])
        return math.gcd(math.gcd(a, b), c)
    return None