def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(lst[86], gcf(lst[89], lst[49]))