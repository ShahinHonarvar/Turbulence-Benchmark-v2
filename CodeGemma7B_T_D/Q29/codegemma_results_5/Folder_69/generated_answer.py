def gcf_two_nums(lst):
    num1 = lst[894]
    num2 = lst[801]
    common_factor = 1
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    common_factor = num1
    return common_factor