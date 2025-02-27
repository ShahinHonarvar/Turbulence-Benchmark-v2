def gcf_three_nums(lst):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(lst[14], gcf(lst[21], lst[17]))