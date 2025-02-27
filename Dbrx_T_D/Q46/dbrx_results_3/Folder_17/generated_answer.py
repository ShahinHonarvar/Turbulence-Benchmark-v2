from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[20]
    num2 = numbers[51]
    num3 = numbers[62]
    common_factor1 = gcd(num1, num2)
    common_factor2 = gcd(common_factor1, num3)
    return common_factor2