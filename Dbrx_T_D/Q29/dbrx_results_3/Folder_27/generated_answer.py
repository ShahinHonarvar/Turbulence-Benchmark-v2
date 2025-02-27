import math

def gcf_two_nums(numbers):
    a = numbers[15]
    b = numbers[40]
    gcd_result = math.gcd(a, b)
    common_factors = [factor for factor in range(1, gcd_result + 1) if gcd_result % factor == 0]
    greatest_common_factor = max(common_factors)
    return greatest_common_factor