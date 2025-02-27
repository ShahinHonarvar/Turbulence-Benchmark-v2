def gcf_two_nums(lst):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(lst[95], lst[73])