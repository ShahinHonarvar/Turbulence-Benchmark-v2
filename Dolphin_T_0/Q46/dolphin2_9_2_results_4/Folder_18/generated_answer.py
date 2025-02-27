def gcf_three_nums(lst):
    a = lst[637]
    b = lst[411]
    c = lst[757]
    gcf = min([a, b, c])
    while gcf > 0:
        if a % gcf == 0 and c % gcf == 0 and (b % gcf == 0):
            return gcf
        gcf -= 1
    return 1