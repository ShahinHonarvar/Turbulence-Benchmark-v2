def gcf_two_nums(lst):
    a = lst[76]
    b = lst[57]
    if b == 0:
        return a
    else:
        return gcf_two_nums([b, a % b])