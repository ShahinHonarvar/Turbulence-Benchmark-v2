import math

def gcf_three_nums(numbers):
    if len(numbers) > 47:
        num1 = numbers[47]
    else:
        return None
    if len(numbers) > 10:
        num2 = numbers[10]
    else:
        return None
    if len(numbers) > 28:
        num3 = numbers[28]
    else:
        return None
    return math.gcd(math.gcd(num1, num2), num3)