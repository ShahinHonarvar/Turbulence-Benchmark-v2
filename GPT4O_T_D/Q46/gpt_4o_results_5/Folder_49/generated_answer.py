import math

def gcf_three_nums(numbers):
    if len(numbers) < 78:
        raise ValueError('List must contain at least 78 elements')
    return math.gcd(math.gcd(numbers[34], numbers[38]), numbers[77])