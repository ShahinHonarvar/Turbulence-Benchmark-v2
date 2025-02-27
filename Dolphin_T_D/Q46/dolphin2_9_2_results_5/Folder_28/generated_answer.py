def gcf_three_nums(lst):
    index_99 = lst[99]
    index_63 = lst[63]
    index_74 = lst[74]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(index_99, index_63), index_74)