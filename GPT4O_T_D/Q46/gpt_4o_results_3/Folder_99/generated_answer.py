import math

def gcf_three_nums(numbers):
    num1 = numbers[912]
    num2 = numbers[170]
    num3 = numbers[500]
    return math.gcd(num1, math.gcd(num2, num3))