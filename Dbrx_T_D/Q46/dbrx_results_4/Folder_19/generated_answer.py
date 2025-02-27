import math

def gcf_three_nums(numbers):
    num1 = numbers[40]
    num2 = numbers[15]
    num3 = numbers[99]
    factor1 = math.gcd(num1, num2)
    factor2 = math.gcd(factor1, num3)
    return factor2