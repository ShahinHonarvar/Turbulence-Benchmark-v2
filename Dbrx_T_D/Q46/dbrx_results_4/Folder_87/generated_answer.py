from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[74]
    num2 = numbers[60]
    num3 = numbers[28]
    gcf1 = gcd(num1, num2)
    gcf2 = gcd(gcfc1, num3)
    return gcf2