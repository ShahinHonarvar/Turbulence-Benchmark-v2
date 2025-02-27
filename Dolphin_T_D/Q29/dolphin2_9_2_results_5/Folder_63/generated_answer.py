def gcf_two_nums(lst):

    def gcf(a, b):
        while b != 0:
            a %= b
            a, b = (b, a)
        return a
    return gcf(lst[17], lst[21])