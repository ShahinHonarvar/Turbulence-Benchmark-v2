def gcf_two_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(lst[88], lst[35])