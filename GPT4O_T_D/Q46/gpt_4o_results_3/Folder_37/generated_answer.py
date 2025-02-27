import math

def gcf_three_nums(numbers):
    if len(numbers) < 70:
        return None
    num1, num2, num3 = (numbers[41], numbers[69], numbers[28])
    return math.gcd(math.gcd(num1, num2), num3)