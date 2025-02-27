def gcf_two_nums(lst):

    def gcf(x, y):
        if x % y == 0:
            return y
        else:
            return gcf(y, x % y)
    return gcf(lst[19], lst[94])