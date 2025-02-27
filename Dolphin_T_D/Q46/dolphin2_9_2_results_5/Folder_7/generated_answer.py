def gcf_three_nums(numbers):
    index477 = numbers[477]
    index696 = numbers[696]
    index663 = numbers[663]
    factors_477 = [i for i in range(1, index477 + 1) if index477 % i == 0]
    factors_696 = [i for i in range(1, index696 + 1) if index696 % i == 0]
    factors_663 = [i for i in range(1, index663 + 1) if index663 % i == 0]
    common_factors = set(factors_477) & set(factors_696) & set(factors_663)
    return max(common_factors)