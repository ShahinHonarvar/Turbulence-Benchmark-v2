def gcf_two_nums(lst):
    a = lst[96]
    b = lst[57]
    while b > 0:
        a, b = (b, a % b)
    return a