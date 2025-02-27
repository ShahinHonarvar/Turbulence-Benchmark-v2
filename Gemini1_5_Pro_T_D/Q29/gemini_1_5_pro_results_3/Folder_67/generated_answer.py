def gcf_two_nums(lst):
    a = lst[64]
    b = lst[28]
    while b:
        a, b = (b, a % b)
    return a