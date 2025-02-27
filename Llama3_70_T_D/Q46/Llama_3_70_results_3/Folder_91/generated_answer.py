def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[8], lst[9], lst[3])
    return gcf(gcf(a, b), c)