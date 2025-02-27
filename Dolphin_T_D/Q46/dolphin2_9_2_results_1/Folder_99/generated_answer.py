def gcf_three_nums(lst):
    a = lst[912]
    b = lst[170]
    c = lst[500]

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(a, b), c)