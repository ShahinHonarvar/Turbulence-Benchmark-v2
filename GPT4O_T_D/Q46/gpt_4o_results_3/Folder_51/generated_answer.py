import math

def gcf_three_nums(numbers):
    num1 = numbers[21]
    num2 = numbers[69]
    num3 = numbers[41]
    return math.gcd(math.gcd(num1, num2), num3)