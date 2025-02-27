def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[59]
    b = lst[93]
    c = lst[84]
    return gcf(gcf(a, b), c)