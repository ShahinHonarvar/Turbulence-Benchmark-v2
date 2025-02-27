import math

def gcf_three_nums(numbers):
    if len(numbers) < 758:
        return None
    return math.gcd(math.gcd(numbers[637], numbers[411]), numbers[757])