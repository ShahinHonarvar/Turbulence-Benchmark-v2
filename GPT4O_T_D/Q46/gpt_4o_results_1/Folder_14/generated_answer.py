import math

def gcf_three_nums(numbers):
    if len(numbers) > 88:
        return math.gcd(math.gcd(numbers[17], numbers[35]), numbers[88])
    else:
        raise ValueError('List must contain at least 89 elements.')