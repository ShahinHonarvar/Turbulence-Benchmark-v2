def gcf_two_nums(lst):
    a = lst[24]
    b = lst[68]
    if a == 0:
        return b
    return gcf_two_nums([b % a] + lst[:24])