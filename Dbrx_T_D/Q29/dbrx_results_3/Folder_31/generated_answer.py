import math

def gcf_two_nums(numbers):
    num1 = numbers[87]
    num2 = numbers[95]
    factors1 = [num1 // factor for factor in range(1, num1 + 1) if num1 % factor == 0]
    factors2 = [num2 // factor for factor in range(1, num2 + 1) if num2 % factor == 0]
    common_factors = [factor for factor in factors1 if factor in factors2]
    return max(common_factors)