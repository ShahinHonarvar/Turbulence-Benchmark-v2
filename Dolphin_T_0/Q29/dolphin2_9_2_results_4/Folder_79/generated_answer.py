def gcf_two_nums(lst):

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(lst[85], lst[51])