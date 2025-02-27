import math

def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[637]
    num2 = numbers[411]
    num3 = numbers[757]
    return gcd(gcd(num1, num2), num3)