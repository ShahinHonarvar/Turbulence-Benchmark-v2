def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = lst[13]
    b = lst[76]
    c = lst[44]
    return gcf(gcf(a, b), c)