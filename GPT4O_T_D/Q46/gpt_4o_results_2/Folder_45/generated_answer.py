import math

def gcf_three_nums(numbers):
    if len(numbers) <= max(46, 84, 23):
        return None
    num1 = numbers[46]
    num2 = numbers[84]
    num3 = numbers[23]
    return math.gcd(math.gcd(num1, num2), num3)