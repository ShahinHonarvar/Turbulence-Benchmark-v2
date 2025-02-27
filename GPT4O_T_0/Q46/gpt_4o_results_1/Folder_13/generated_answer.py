import math

def gcf_three_nums(numbers):
    if len(numbers) < 975:
        return None
    return math.gcd(math.gcd(numbers[991], numbers[244]), numbers[974])