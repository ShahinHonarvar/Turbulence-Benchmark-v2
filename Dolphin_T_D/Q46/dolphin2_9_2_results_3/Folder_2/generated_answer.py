def gcf_three_nums(lst):
    num1 = lst[307]
    num2 = lst[920]
    num3 = lst[463]
    gcf = min(num1, num2, num3)
    while True:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            return gcf
        else:
            gcf -= 1