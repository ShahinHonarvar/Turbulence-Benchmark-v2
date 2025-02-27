import math

def gcf_three_nums(numbers):
    if len(numbers) < 29:
        return None
    return math.gcd(math.gcd(numbers[20], numbers[17]), numbers[28])