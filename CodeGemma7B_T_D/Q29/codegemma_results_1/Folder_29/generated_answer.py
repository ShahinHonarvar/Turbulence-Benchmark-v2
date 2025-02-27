def gcf_two_nums(lst):
    a = lst[96]
    b = lst[57]
    g = a if a < b else b
    while a % g != 0 or b % g != 0:
        g -= 1
    return g