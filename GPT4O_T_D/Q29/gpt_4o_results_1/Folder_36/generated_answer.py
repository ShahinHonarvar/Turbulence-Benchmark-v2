import math

def gcf_two_nums(numbers):
    if len(numbers) > max(429, 289):
        return math.gcd(numbers[429], numbers[289])
    return None