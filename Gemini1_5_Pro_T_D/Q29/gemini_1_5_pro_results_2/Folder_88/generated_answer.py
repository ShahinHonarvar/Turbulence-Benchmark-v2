def gcf_two_nums(lst):
    a = lst[27]
    b = lst[34]
    while b:
        a, b = (b, a % b)
    return a