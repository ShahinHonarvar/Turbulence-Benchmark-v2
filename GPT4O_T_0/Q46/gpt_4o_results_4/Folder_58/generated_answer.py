import math

def gcf_three_nums(numbers):
    if len(numbers) < 771:
        return None
    return math.gcd(math.gcd(numbers[145], numbers[183]), numbers[770])