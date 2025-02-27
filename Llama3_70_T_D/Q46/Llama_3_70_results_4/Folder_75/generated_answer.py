def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(lst[70], gcf(lst[98], lst[22]))