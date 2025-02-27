import math

def gcf_three_nums(numbers):
    a = numbers[20]
    b = numbers[43]
    c = numbers[95]
    factor_a = [factor for factor in range(1, a + 1) if a % factor == 0]
    factor_b = [factor for factor in range(1, b + 1) if b % factor == 0]
    factor_c = [factor for factor in range(1, c + 1) if c % factor == 0]
    common_factors = list(set(factor_a) & set(factor_b) & set(factor_c))
    return max(common_factors)