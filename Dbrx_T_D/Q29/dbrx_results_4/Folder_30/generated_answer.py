import math

def gcf_two_nums(numbers):
    num1 = numbers[85]
    num2 = numbers[33]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    common_factors = [i for i in factors1 if i in factors2]
    return max(common_factors)