import math

def gcf_three_nums(numbers):
    if len(numbers) < 75:
        return None
    x = numbers[29]
    y = numbers[74]
    z = numbers[49]
    return math.gcd(math.gcd(x, y), z)