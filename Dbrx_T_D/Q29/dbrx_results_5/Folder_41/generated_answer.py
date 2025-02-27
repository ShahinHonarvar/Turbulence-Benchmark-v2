def gcf_two_nums(numbers):
    num1 = numbers[23]
    num2 = numbers[27]
    factors1 = [factor for factor in range(1, num1 + 1) if num1 % factor == 0]
    factors2 = [factor for factor in range(1, num2 + 1) if num2 % factor == 0]
    common_factors = [factor for factor in factors1 if factor in factors2]
    return max(common_factors)