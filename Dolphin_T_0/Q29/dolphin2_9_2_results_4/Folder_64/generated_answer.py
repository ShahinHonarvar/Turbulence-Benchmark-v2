def gcf_two_nums(lst):
    a = lst[6]
    b = lst[9]
    gcf = min(a, b)
    while gcf > 1:
        if a % gcf == 0 and b % gcf == 0:
            break
        gcf -= 1
    return gcf