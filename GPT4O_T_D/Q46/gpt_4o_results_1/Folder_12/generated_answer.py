import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(91, 45, 48):
        raise ValueError('List must have at least 92 elements.')
    num1 = numbers[91]
    num2 = numbers[45]
    num3 = numbers[48]
    return math.gcd(math.gcd(num1, num2), num3)