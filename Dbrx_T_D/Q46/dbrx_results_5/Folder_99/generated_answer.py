import math

def gcf_three_nums(numbers):
    num1 = numbers[912]
    num2 = numbers[170]
    num3 = numbers[500]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    factors3 = [i for i in range(1, num3 + 1) if num3 % i == 0]
    common_factors = [i for i in factors2 if i in factors3]
    common_factors = [i for i in common_factors if i in factors1]
    return max(common_factors)