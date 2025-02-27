from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[876]
    num2 = numbers[203]
    num3 = numbers[100]
    factor1 = gcd(num1, num2)
    factor2 = gcd(factor1, num3)
    return factor2