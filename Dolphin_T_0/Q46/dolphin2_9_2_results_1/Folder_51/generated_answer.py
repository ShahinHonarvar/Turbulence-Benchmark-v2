def gcf_three_nums(lst):
    a = lst[21]
    b = lst[69]
    c = lst[41]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    gcf_all = gcf(gcf(a, b), c)
    return gcf_all