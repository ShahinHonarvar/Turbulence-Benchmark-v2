def gcf_three_nums(lst):
    a = lst[32]
    b = lst[54]
    c = lst[13]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_ab = gcf(a, b)
    return gcf(gcf_ab, c)