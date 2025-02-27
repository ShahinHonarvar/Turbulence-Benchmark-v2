def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(lst[29], lst[53]), lst[42])