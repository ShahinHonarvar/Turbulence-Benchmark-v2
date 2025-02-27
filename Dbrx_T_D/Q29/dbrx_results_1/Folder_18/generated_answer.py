import math

def gcf_two_nums(numbers):
    num1 = numbers[872]
    num2 = numbers[219]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [j for j in range(1, num2 + 1) if num2 % j == 0]
    gcd = max([f for f in factors1 if f in factors2])
    factors_gcd = [i for i in range(1, gcd + 1) if gcd % i == 0]
    return max(factors_gcd)