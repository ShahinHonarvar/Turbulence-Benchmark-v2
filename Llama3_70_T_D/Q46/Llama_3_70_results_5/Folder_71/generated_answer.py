def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[24], lst[45], lst[38])
    return gcf(gcf(a, b), c)