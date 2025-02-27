def gcf_two_nums(lst):
    a = lst[85]
    b = lst[51]
    while b:
        a, b = (b, a % b)
    return a