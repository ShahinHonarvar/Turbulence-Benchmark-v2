def gcf_three_nums(lst):
    num1 = lst[13]
    num2 = lst[76]
    num3 = lst[44]
    gcf = min(num1, num2, num3)
    while True:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            return gcf
        else:
            gcf -= 1