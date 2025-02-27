import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(307, 920, 463):
        return None
    return math.gcd(math.gcd(numbers[307], numbers[920]), numbers[463])