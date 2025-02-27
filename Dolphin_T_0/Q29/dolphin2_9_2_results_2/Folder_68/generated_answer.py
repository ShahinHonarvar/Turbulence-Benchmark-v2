def gcf_two_nums(lst):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(lst[8], lst[9])