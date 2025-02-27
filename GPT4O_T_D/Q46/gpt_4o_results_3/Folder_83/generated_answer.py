import math

def gcf_three_nums(numbers):
    if len(numbers) > max(56, 54, 13):
        num1 = numbers[56]
        num2 = numbers[54]
        num3 = numbers[13]
        return math.gcd(math.gcd(num1, num2), num3)
    else:
        return None