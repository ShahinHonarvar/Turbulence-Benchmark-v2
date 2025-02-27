def gcf_three_nums(lst):
    num1 = lst[56]
    num2 = lst[88]
    num3 = lst[51]
    gcf = min(num1, num2, num3)
    while True:
        if num1 % gcf == 0 and num2 % gcf == 0 and (num3 % gcf == 0):
            break
        else:
            gcf -= 1
    return gcf