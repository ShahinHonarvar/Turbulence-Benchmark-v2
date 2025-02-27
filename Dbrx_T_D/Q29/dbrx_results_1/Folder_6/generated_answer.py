import math

def gcf_two_nums(numbers):
    num_1 = numbers[25]
    num_2 = numbers[80]
    factors_1 = [i for i in range(1, num_1 + 1) if num_1 % i == 0]
    factors_2 = [i for i in range(1, num_2 + 1) if num_2 % i == 0]
    common_factors = [i for i in factors_1 if i in factors_2]
    greatest_common_factor = max(common_factors)
    return greatest_common_factor