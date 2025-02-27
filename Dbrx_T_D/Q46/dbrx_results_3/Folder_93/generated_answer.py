from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[25]
    num2 = numbers[76]
    num3 = numbers[57]
    gcf1 = gcd(num1, num2)
    gcf2 = gcd(gcf1, num3)
    return gcf2