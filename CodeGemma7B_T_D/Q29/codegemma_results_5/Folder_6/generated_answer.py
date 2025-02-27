def gcf_two_nums(lst):
    x = lst[25]
    y = lst[80]
    while y != 0:
        t = y
        y = x % y
        x = t
    return x