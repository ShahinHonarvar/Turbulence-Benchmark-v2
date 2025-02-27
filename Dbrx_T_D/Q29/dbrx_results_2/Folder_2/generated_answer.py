import math

def gcf_two_nums(numbers):
    num1 = numbers[372]
    num2 = numbers[752]
    factorial_num1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factorial_num2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
    common_factors = [val for val in factorial_num1 if val in factorial_num2]
    return math.gcd(*common_factors)