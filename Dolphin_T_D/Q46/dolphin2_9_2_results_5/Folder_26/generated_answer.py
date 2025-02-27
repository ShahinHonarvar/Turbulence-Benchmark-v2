def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    index_15 = lst[15]
    index_51 = lst[51]
    index_76 = lst[76]
    gcf_value = gcf(index_15, gcf(index_51, index_76))
    return gcf_value