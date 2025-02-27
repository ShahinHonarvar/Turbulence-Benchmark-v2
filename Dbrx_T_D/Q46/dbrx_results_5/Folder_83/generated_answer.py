import math

def gcf_three_nums(numbers):

    def gcd(a, b):
        return math.gcd(a, b) if b != 0 else a
    num1 = numbers[56]
    num2 = numbers[54]
    num3 = numbers[13]
    return gcd(gcd(num1, num2), num3)