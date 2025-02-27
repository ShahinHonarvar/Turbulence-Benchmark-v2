def gcf_two_nums(lst):
    num1 = lst[20]
    num2 = lst[28]
    common_factor = 2
    for i in range(2, min([num1, num2]) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factor = i
    return common_factor