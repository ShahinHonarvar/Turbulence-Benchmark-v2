def gcf_two_nums(lst):
    if len(lst) < 10:
        return None
    num1 = lst[8]
    num2 = lst[9]
    gcf = min(num1, num2)
    while gcf > 0:
        if num1 % gcf == 0 and num2 % gcf == 0:
            return gcf
        gcf -= 1
    return None