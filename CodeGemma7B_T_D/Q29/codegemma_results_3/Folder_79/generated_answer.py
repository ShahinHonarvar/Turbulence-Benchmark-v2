def gcf_two_nums(list):
    a = list[85]
    b = list[51]
    if b == 0:
        return a
    return gcf_two_nums(list, b, a % b)