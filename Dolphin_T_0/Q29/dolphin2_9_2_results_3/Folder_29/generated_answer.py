def gcf_two_nums(lst):

    def gcf(a, b):
        if a < b:
            a, b = (b, a)
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(lst[96], lst[57])