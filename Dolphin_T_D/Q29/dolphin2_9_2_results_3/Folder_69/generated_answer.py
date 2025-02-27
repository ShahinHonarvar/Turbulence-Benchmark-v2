def gcf_two_nums(lst):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(lst[894], lst[801])