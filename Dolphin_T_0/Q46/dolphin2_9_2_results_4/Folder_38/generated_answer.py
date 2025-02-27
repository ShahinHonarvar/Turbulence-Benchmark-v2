def gcf_three_nums(lst):
    a = lst[14]
    b = lst[21]
    c = lst[17]
    gcf = min(a, b, c)
    while gcf > 1:
        if a % gcf == 0 and b % gcf == 0 and (c % gcf == 0):
            return gcf
        gcf -= 1
    return 1