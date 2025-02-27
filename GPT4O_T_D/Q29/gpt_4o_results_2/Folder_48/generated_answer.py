import math

def gcf_two_nums(numbers):
    if len(numbers) > 618 and len(numbers) > 195:
        return math.gcd(numbers[618], numbers[195])
    return None