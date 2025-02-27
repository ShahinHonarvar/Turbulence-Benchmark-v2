import math

def gcf_three_nums(numbers):
    if len(numbers) <= 74:
        return None
    return math.gcd(math.gcd(numbers[20], numbers[35]), numbers[74])