def gcf_two_nums(lst):
    a = lst[90]
    b = lst[41]
    while b:
        a, b = (b, a % b)
    return a