import math

def gcf_three_nums(numbers):
    if len(numbers) <= 97:
        return None
    return math.gcd(math.gcd(numbers[19], numbers[69]), numbers[97])