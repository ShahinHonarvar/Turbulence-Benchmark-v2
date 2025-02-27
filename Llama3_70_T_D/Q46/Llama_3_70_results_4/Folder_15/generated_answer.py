def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf_0_4 = gcf(lst[0], lst[4])
    return gcf(gcf_0_4, lst[8])