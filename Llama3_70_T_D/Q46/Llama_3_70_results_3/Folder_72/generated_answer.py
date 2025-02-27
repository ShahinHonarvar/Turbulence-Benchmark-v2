def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[44], lst[91], lst[42])
    return gcf(gcf(a, b), c)