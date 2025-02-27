def gcf_three_nums(lst):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(lst[78], gcf(lst[19], lst[13]))