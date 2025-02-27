def gcf_three_nums(lst):
    num1 = lst[7]
    num2 = lst[6]
    num3 = lst[8]
    common_factor = 0
    for i in range(2, num1 + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            common_factor = i
    return common_factor