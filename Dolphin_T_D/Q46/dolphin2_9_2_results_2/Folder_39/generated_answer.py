def gcf_three_nums(lst):
    num1 = lst[85]
    num2 = lst[36]
    num3 = lst[54]
    gcf = min(num1, num2, num3)
    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            return gcf
        gcf -= 1
    return 1