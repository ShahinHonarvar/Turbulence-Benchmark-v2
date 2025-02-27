def gcf_two_nums(lst):
    a = lst[23]
    b = lst[27]
    while b:
        a, b = (b, a % b)
    return a