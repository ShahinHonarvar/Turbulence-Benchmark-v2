def gcf_two_nums(lst):
    a = lst[7]
    b = lst[9]
    if a == 0:
        return b
    return gcf_two_nums([b % a] + lst[:7] + lst[8:])