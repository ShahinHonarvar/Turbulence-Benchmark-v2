def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(lst[14], gcf(lst[21], lst[17]))