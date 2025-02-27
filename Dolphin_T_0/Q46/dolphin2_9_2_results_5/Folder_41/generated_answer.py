def gcf_three_nums(lst):
    a = lst[19]
    b = lst[94]
    c = lst[78]
    gcf = min(a, b, c)
    while gcf > 1:
        if a % gcf == 0 and b % gcf == 0 and (c % gcf == 0):
            break
        else:
            gcf -= 1
    return gcf