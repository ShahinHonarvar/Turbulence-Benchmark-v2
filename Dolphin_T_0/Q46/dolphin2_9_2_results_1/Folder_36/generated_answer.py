def gcf_three_nums(lst):
    num1 = lst[427]
    num2 = lst[761]
    num3 = lst[148]
    gcf = num1
    while num2 != 0 and num3 != 0:
        if num1 >= num2 and num1 >= num3:
            num1 %= num2 + num3
        elif num2 >= num1 and num2 >= num3:
            num2 %= num1 + num3
        else:
            num3 %= num1 + num2
    return gcf