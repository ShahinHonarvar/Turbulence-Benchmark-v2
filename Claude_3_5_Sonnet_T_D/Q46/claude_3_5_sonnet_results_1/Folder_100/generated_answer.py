import math

def gcf_three_nums(numbers):
    if len(numbers) < 52:
        return None
    num1 = numbers[21]
    num2 = numbers[33]
    num3 = numbers[51]
    return math.gcd(math.gcd(num1, num2), num3)