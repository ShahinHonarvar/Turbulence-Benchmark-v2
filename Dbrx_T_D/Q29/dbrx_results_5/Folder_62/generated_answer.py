import math

def gcf_two_nums(lst):
    num1, num2 = (lst[51], lst[31])
    return math.gcd(num1, num2) if num1 % num2 == 0 else num2 // math.gcd(num1, num2) if num2 % num1 == 0 else math.gcd(num1, num2)