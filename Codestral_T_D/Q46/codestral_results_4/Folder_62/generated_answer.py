import math

def gcf_three_nums(numbers):
    num1 = numbers[10]
    num2 = numbers[55]
    num3 = numbers[36]
    return math.gcd(math.gcd(num1, num2), num3)