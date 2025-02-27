def gcf_two_nums(numbers):
    first_num = numbers[372]
    second_num = numbers[752]
    factors_1 = get_factors(first_num)
    factors_2 = get_factors(second_num)
    common_factors = [factor for factor in factors_1 if factor in factors_2]
    return max(common_factors)

def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors