from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[307]
    num2 = numbers[920]
    num3 = numbers[463]
    return gcd(num1, gcd(num2, num3))