def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = lst[90]
    b = lst[41]
    c = lst[95]
    return gcf(gcf(a, b), c)