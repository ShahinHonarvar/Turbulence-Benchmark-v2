def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[92], lst[69], lst[95])
    return gcf(gcf(a, b), c)