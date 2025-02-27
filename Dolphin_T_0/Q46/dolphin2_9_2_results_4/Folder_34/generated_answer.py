def gcf_three_nums(lst):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(gcf(lst[53], lst[23]), lst[45])