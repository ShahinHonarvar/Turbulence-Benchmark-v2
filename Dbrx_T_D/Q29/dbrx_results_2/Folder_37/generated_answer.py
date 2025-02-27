from math import gcd

def gcf_two_nums(numbers):
    num1 = numbers[29]
    num2 = numbers[74]
    return gcd(num1, num2) if num1 > 0 and num2 > 0 else 0