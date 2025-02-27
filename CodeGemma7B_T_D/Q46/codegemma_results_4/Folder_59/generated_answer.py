def gcf_three_nums(list):
    num1, num2, num3 = (list[7], list[6], list[8])
    common_factors = []
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            common_factors.append(i)
    return max(common_factors)