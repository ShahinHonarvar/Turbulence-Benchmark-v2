def gcf_two_nums(lst):
    a = lst[184]
    b = lst[307]
    while b:
        a, b = (b, a % b)
    return a