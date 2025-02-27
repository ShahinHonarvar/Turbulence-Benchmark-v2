def gcf_two_nums(lst):
    num1 = lst[184]
    num2 = lst[307]
    factors_num1 = []
    factors_num2 = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            factors_num1.append(i)
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            factors_num2.append(i)
    common_factors = []
    for num in factors_num1:
        if num in factors_num2:
            common_factors.append(num)
    return max(common_factors)