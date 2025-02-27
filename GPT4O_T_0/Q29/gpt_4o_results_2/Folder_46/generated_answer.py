import math

def gcf_two_nums(numbers):
    if len(numbers) > 54:
        return math.gcd(numbers[36], numbers[54])
    return None