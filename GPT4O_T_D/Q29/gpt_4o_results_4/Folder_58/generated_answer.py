import math

def gcf_two_nums(numbers):
    if len(numbers) < 583:
        return None
    return math.gcd(numbers[129], numbers[582])