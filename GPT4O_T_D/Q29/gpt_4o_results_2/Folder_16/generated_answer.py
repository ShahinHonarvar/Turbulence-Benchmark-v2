import math

def gcf_two_nums(numbers):
    if len(numbers) > 860:
        num1 = numbers[860]
    else:
        return None
    if len(numbers) > 307:
        num2 = numbers[307]
    else:
        return None
    return math.gcd(num1, num2)