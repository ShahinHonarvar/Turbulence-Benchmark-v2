def gcf_three_nums(lst):
    num1 = lst[85]
    num2 = lst[36]
    num3 = lst[54]
    common_factors = []
    for i in range(1, min([num1, num2, num3]) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            common_factors.append(i)
    return max(common_factors)