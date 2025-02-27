import math

def gcf_three_nums(numbers):
    a, b, c = (numbers[40], numbers[15], numbers[99])

    def is_factor(x, y):
        return y % x == 0
    factors_a = [x for x in range(1, a + 1) if is_factor(x, a)]
    factors_b = [x for x in range(1, b + 1) if is_factor(x, b)]
    factors_c = [x for x in range(1, c + 1) if is_factor(x, c)]
    common_factors = [x for x in factors_a if x in factors_b and x in factors_c]
    if common_factors:
        return max(common_factors)
    else:
        return 1