def gcf_two_nums(lst):
    a = lst[83]
    b = lst[14]
    if a == 0:
        return b
    return gcf_two_nums([b % a] + lst[:83])