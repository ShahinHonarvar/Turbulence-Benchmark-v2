def gcf_two_nums(lst):
    a = lst[60]
    b = lst[64]
    while b:
        a, b = (b, a % b)
    return a