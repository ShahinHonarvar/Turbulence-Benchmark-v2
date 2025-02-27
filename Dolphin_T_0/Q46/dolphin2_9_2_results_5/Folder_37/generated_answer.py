def gcf_three_nums(lst):
    num1 = lst[41]
    num2 = lst[69]
    num3 = lst[28]
    gcf = min(num1, num2, num3)
    while num1 % gcf != 0 or num2 % gcf != 0 or num3 % gcf != 0:
        gcf -= 1
    return gcf