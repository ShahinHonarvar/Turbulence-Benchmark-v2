import math

def gcf_three_nums(numbers):
    if len(numbers) < 96:
        return None
    a, b, c = (numbers[92], numbers[69], numbers[95])
    return math.gcd(math.gcd(a, b), c)