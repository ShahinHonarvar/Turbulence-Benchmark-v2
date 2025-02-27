import math

def gcf_three_nums(numbers):
    if len(numbers) < 913 or len(numbers) < 171 or len(numbers) < 501:
        return None
    num1 = numbers[912]
    num2 = numbers[170]
    num3 = numbers[500]
    return math.gcd(math.gcd(num1, num2), num3)