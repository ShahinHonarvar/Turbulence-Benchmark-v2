def gcf_three_nums(lst):
    a = lst[13]
    b = lst[76]
    c = lst[44]

    def gcf(a, b):
        while b != 0:
            a = a % b
            a, b = (b, a)
        return a
    if b == 0:
        return a
    res = gcf(a, b)
    res = gcf(res, c)
    return res