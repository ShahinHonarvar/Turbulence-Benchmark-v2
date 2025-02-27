from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[63]
    num2 = numbers[73]
    num3 = numbers[11]
    factor1 = gcd(num1, num2)
    factor2 = gcd(factor1, num3)
    return factor2