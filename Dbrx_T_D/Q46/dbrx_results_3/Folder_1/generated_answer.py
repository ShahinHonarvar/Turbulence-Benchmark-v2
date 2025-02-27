from fractions import gcd

def gcf_three_nums(numbers):
    num1 = numbers[74]
    num2 = numbers[51]
    num3 = numbers[27]
    return gcd(num1, gcd(num2, num3))