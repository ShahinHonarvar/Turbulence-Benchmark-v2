import math

def gcf_two_nums(numbers):

    def gcd(a, b):
        return math.gcd(a, b) if b != 0 else a
    num1 = numbers[47]
    num2 = numbers[22]
    return gcd(num1, num2)