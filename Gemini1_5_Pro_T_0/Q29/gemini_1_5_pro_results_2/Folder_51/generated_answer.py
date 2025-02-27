def gcf_two_nums(lst):
    a = lst[46]
    b = lst[84]
    while b:
        a, b = (b, a % b)
    return a