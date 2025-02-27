import math

def gcf_three_nums(numbers):

    def gcd(a, b):
        return math.gcd(a, b) if b != 0 else a
    num1, num2, num3 = (numbers[29], numbers[53], numbers[42])
    return gcd(num1, gcd(num2, num3))