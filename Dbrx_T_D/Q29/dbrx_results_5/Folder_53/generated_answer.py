import math

def gcf_two_nums(numbers):
    num1 = numbers[28]
    num2 = numbers[67]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    common_factors = [factor for factor in factors1 if factor in factors2]
    return max(common_factors)