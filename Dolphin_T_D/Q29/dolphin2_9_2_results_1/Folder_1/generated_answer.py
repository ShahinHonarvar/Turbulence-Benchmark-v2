def gcf_two_nums(lst):
    a = lst[13]
    b = lst[66]
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcf_two_nums([b % a] + lst[:-1])