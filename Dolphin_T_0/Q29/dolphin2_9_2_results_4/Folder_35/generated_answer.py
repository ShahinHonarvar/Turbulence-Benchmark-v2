def gcf_two_nums(lst):
    a = lst[380]
    b = lst[327]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a