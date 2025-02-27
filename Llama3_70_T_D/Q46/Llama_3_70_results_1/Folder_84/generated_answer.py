def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    idx_695 = lst[695]
    idx_710 = lst[710]
    idx_914 = lst[914]
    result = gcf(idx_695, idx_710)
    result = gcf(result, idx_914)
    return result