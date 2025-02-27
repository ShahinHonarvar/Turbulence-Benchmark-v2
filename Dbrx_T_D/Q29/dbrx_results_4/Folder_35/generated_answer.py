from math import gcd

def gcf_two_nums(numbers):
    num1 = numbers[380]
    num2 = numbers[327]
    return gcd(num1, num2) if num1 != num2 else num1