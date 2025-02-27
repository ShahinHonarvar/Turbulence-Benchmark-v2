def gcf_three_nums(num_lst):
    num1 = num_lst[10]
    num2 = num_lst[55]
    num3 = num_lst[36]
    common_factor = 1
    for i in range(2, min([num1, num2, num3]) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            common_factor = i
    return common_factor