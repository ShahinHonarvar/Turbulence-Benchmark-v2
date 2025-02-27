def gcf_two_nums(lst):
    a = lst[15]
    b = lst[99]
    while b:
        a, b = (b, a % b)
    return a