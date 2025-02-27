import math

def gcf_two_nums(numbers):

    def gcd(a, b):
        return math.gcd(a, b) if b != 0 else a
    num1 = numbers[86]
    num2 = numbers[89]
    gcf_value = gcd(num1, num2)
    return gcf_value