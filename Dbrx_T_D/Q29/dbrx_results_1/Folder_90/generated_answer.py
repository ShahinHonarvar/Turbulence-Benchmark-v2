import math

def gcf_two_nums(numbers):
    num1 = numbers[634]
    num2 = numbers[585]

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    gcf = gcd(num1, num2)
    return gcf