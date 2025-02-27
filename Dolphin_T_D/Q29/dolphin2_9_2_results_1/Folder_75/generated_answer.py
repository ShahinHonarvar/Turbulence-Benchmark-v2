def gcf_two_nums(lst):
    a = lst[42]
    b = lst[25]
    if a == 0:
        return b
    return gcf_two_nums([b % a] + lst)