def gcf_two_nums(lst):
    a = lst[29]
    b = lst[53]
    if a == 0:
        return b
    return gcf_two_nums([a % b, b])