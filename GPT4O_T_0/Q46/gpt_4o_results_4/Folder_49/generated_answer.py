import math

def gcf_three_nums(numbers):
    if len(numbers) < 78:
        return None
    return math.gcd(math.gcd(numbers[34], numbers[38]), numbers[77])