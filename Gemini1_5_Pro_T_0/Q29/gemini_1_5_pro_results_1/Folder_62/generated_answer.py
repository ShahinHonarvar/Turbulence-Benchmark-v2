def gcf_two_nums(lst):
    a = lst[51]
    b = lst[31]
    while b:
        a, b = (b, a % b)
    return a