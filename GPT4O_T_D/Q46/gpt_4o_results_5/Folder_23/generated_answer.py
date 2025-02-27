import math

def gcf_three_nums(numbers):
    if len(numbers) < 81:
        return None
    num1 = numbers[31]
    num2 = numbers[25]
    num3 = numbers[80]
    return math.gcd(math.gcd(num1, num2), num3)