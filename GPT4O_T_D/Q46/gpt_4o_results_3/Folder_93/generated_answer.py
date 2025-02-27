import math

def gcf_three_nums(numbers):
    if len(numbers) > 76:
        return math.gcd(math.gcd(numbers[25], numbers[76]), numbers[57])
    return None