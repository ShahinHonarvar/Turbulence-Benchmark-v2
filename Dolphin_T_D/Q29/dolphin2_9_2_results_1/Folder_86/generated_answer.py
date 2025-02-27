def gcf_two_nums(lst):

    def gcf(a, b):
        if a % b == 0:
            return b
        return gcf(b, a % b)
    return gcf(lst[793], lst[449])