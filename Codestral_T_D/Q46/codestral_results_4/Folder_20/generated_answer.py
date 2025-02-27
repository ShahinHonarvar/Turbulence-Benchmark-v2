import math

def gcf_three_nums(numbers):
    num1 = numbers[29]
    num2 = numbers[53]
    num3 = numbers[42]
    return math.gcd(math.gcd(num1, num2), num3)