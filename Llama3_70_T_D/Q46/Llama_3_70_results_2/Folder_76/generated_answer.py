def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[876], lst[203], lst[100])
    return gcf(gcf(a, b), c)