def gcf_three_nums(a):
    a_37, a_30, a_48 = (a[37], a[30], a[48])
    gcf = a_37
    while a_30 % gcf != 0 or a_48 % gcf != 0:
        gcf -= 1
    return gcf