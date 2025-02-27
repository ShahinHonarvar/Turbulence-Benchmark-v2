def gcf_two_nums(lst):
    a = lst[8]
    b = lst[9]
    if a == 0:
        return b
    return gcf_two_nums([b % a, a])