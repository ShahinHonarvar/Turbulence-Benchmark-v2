def gcf_three_nums(lst):
    a = lst[8]
    b = lst[2]
    c = lst[1]
    gcf = int(a)
    while gcf > 1:
        if a % gcf == 0 and b % gcf == 0 and (c % gcf == 0):
            break
        else:
            gcf -= 1
    return gcf