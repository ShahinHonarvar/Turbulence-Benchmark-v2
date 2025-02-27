import math

def gcf_three_nums(numbers):
    if len(numbers) > max(17, 88, 35):
        return math.gcd(math.gcd(numbers[17], numbers[88]), numbers[35])
    else:
        return None