def gcf_three_nums(lst):
    num1 = lst[96]
    num2 = lst[53]
    num3 = lst[35]
    gcf = min(num1, num2, num3)
    while True:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            return gcf
        gcf -= 1