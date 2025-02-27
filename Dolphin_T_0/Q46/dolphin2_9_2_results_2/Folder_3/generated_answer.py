def gcf_three_nums(lst):
    num1 = lst[31]
    num2 = lst[69]
    num3 = lst[40]
    gcf = num1
    while num2 != 0 and num3 != 0:
        if num3 > num2:
            num3 = num2
        else:
            num2 = num3
        gcf = num2
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return gcf