import math

def gcf_three_nums(numbers):
    if len(numbers) > max(90, 84, 47):
        return math.gcd(math.gcd(numbers[90], numbers[84]), numbers[47])
    return None