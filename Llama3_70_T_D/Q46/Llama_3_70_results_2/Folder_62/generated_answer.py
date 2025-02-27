def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(lst[10], gcf(lst[55], lst[36]))