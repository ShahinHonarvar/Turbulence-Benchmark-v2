import math

def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[8]
    num2 = numbers[9]
    num3 = numbers[3]
    factor1 = gcd(num1, num2)
    factor2 = gcd(factor1, num3)
    return factor2