import math

def gcf_three_nums(numbers):
    if len(numbers) < 913 or len(numbers) < 171 or len(numbers) < 501:
        return None
    return math.gcd(math.gcd(numbers[912], numbers[170]), numbers[500])