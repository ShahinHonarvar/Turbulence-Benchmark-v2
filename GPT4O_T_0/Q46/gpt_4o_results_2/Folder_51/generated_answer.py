import math

def gcf_three_nums(numbers):
    if len(numbers) < 70:
        return None
    return math.gcd(math.gcd(numbers[21], numbers[69]), numbers[41])