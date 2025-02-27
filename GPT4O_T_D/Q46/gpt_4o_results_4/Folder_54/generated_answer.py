import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(96, 57, 85):
        return None
    return math.gcd(math.gcd(numbers[96], numbers[57]), numbers[85])