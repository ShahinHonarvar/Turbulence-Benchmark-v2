import math

def gcf_three_nums(numbers):
    num1 = numbers[78]
    num2 = numbers[19]
    num3 = numbers[13]
    return math.gcd(math.gcd(num1, num2), num3)