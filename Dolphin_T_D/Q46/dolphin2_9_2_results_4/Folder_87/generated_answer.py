def gcf_three_nums(lst):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def gcf_three_nums_lst(lst):
        return gcf(lst[74], gcf(lst[60], lst[28]))
    return gcf_three_nums_lst(lst)