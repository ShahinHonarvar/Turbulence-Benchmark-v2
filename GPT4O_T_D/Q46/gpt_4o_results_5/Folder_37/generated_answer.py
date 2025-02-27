import math

def gcf_three_nums(numbers):
    if len(numbers) > max(41, 69, 28):
        num1 = numbers[41]
        num2 = numbers[69]
        num3 = numbers[28]
        return math.gcd(math.gcd(num1, num2), num3)
    return None