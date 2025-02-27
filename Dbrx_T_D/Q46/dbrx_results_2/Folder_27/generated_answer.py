import math

def gcf_three_nums(numbers):
    a = numbers[76]
    b = numbers[64]
    c = numbers[28]
    factors_a = [i for i in range(1, a + 1) if a % i == 0]
    factors_b = [i for i in range(1, b + 1) if b % i == 0]
    factors_c = [i for i in range(1, c + 1) if c % i == 0]
    common_factors = [i for i in factors_a if i in factors_b and i in factors_c]
    return max(common_factors)