import math

def gcf_three_nums(numbers):
    if len(numbers) > 696:
        a = numbers[477]
        b = numbers[696]
        c = numbers[663]
        return math.gcd(math.gcd(a, b), c)
    else:
        return None