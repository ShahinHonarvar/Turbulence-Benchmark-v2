def gcf_two_nums(lst):
    a = lst[15]
    b = lst[99]
    while b != a:
        if b > a:
            b = b - a
        else:
            a = a - b
    return a