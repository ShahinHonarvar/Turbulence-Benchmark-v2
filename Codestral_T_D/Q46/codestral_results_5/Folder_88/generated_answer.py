def gcf_three_nums(nums_list):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(nums_list[47], nums_list[10]), nums_list[28])