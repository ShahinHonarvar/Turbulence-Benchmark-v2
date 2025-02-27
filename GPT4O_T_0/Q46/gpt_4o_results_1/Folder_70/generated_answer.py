import math

def gcf_three_nums(numbers):
    if len(numbers) < 712:
        return None
    return math.gcd(math.gcd(numbers[990], numbers[671]), numbers[711])