def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(lst[76], lst[35]), lst[74])