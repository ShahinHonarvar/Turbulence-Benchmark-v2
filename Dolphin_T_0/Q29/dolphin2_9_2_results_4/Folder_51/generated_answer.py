def gcf_two_nums(lst):
    if 46 < len(lst) and 84 < len(lst):
        a = lst[46]
        b = lst[84]
        if a == 0:
            return b
        if b == 0:
            return a
        while b:
            a, b = (b, a % b)
        return a
    else:
        return 0