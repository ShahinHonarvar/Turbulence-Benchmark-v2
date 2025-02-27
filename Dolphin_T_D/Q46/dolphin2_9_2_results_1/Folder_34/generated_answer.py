def gcf_three_nums(lst):
    a = lst[53]
    b = lst[23]
    c = lst[45]

    def gcf(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    gcf_ab = gcf(a, b)
    gcf_abc = gcf(gcf_ab, c)
    return gcf_abc