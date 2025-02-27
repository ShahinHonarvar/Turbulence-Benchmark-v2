import math

def gcf_three_nums(numbers):
    num1 = numbers[78]
    num2 = numbers[19]
    num3 = numbers[13]
    gcd1 = math.gcd(num1, num2)
    gcd2 = math.gcd(gcd1, num3)
    return gcd2