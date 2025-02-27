import math

def gcf_three_nums(numbers):
    if len(numbers) < 92:
        return None
    return math.gcd(math.gcd(numbers[44], numbers[91]), numbers[42])